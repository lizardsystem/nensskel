import os
import tempfile

from fabric.api import abort
from fabric.api import env
from fabric.api import local
from fabric.api import sudo
from fabric.context_managers import cd
from fabric.contrib.console import confirm
from fabric.contrib.files import exists
#from fabric.decorators import hosts
#from fabric.operations import get
from fabric.operations import prompt
from fabric.operations import put
from zest.releaser import choose
from zest.releaser.utils import get_last_tag as _get_last_tag

HOSTS = ['TODO']
HOSTNAME = 'TODO'
BASEDIR = '/srv/' + HOSTNAME
PACKAGES = [
    'backupninja',
    'binutils',
    'build-essential',
    'etckeeper',
    'git',
    'zip',
    'unzip',
    'libjpeg-dev',
    'lynx-cur',
    'memcached',
    'nginx',
    'python-dev',
    'python-gdal',
    'python-imaging',
    'python-lxml',
    'python-mapnik',
    'python-matplotlib',
    'python-psycopg2',
    'python-pyproj',
    'python-pysqlite2',
    'python-scipy',
    'python-setuptools',
    'rdiff-backup',
    'spatialite-bin',
    'subversion',
    'unzip',
    ]
BACKUP_SCRIPT = """
when = hourly

[source]
label = websites_var_data
type = local
keep = 30
include = /srv/*/var
exclude = /srv/*/var/cache
exclude = /srv/*/var/static

[dest]
type = local
directory = /var/backups
"""
LOGROTATE_SCRIPT = """
# Mostly copied from ubuntu's standard nginx logrotate script.
/srv/*/var/log/[ae]*.log {
    # [ae]*.log matches access.log and error.log
    # and not django.log and gunicorn*.log.
    weekly
    missingok
    rotate 5
    compress
    delaycompress
    notifempty
    create 0640 www-data adm
    sharedscripts
    prerotate
        if [ -d /etc/logrotate.d/httpd-prerotate ]; then \
            run-parts /etc/logrotate.d/httpd-prerotate; \
        fi; \
    endscript
    postrotate
        [ ! -f /var/run/nginx.pid ] || kill -USR1 `cat /var/run/nginx.pid`
    endscript
}
"""

env['hosts'] = HOSTS
env['sudo_prefix'] += '-H '

DB_USER = 'TODO'
DB_NAME = 'TODO'
DB_HOST = 'TODO'


class _Info(object):
    """Information about the local and remote directory."""
    def __init__(self):
        self.vcs = choose.version_control()
        if self.vcs.internal_filename == '.git':
            self.git = True
            self.svn = False
        else:
            self.git = False
            self.svn = True
        self.last_tag = _get_last_tag(self.vcs)

    def trunk_url(self):
        """Return trunk url (or git origin url)."""
        if hasattr(self, '_trunk_url'):
            return self._trunk_url
        if self.svn:
            self._trunk_url = self.vcs._svn_info()
        if self.git:
            output = local('git remote -v', capture=True)
            lines = output.splitlines()
            lines = [line for line in lines
                     if 'origin' in line and 'fetch' in line]
            if len(lines) != 1:
                print(output)
                abort("Expecting one origin fetch url, got %s" % len(lines))
            line = lines[0]
            # line looks like "origin git@github.com:nens/vss.git (fetch)".
            self._trunk_url = line.split()[1]
        return self._trunk_url

    def initial_checkout_cmd(self):
        """Return command to make an initial svn checkout or git clone."""
        if self.svn:
            return 'svn co %s %s' % (self.trunk_url(), BASEDIR)
        if self.git:
            return 'git clone %s %s' % (self.trunk_url(), BASEDIR)

    def check_srv_availability(self):
        if not exists(BASEDIR):
            print("Directory %s doesn't exist yet" % BASEDIR)
            print("Run fabric with the 'create_srv_dir' command.")


def server_install_ubuntu_packages():
    """Make sure all necessary ubuntu packages are installed."""
    sudo("apt-get install %s" % ' '.join(PACKAGES))


def server_install_backup_and_logrotate_scripts():
    """Configure /etc/something.d/* globally on the server."""
    backup_target = '/etc/backup.d/50-websites-var.rdiff'
    for target, source_string in (
        (backup_target, BACKUP_SCRIPT),
        ('/etc/logrotate.d/websites', LOGROTATE_SCRIPT),
        ):
        if exists(target):
            if not confirm("%s exists, overwrite?" % target,
                           default=False):
                continue
        handle, filename = tempfile.mkstemp()
        open(filename, 'w').write(source_string)
        put(filename, target, use_sudo=True)
        sudo("chown root:root %s" % target)
    # Extras.
    sudo("chmod go-rwx %s" % backup_target)
    sudo("backupninja --test")


def initial_create_srv_dir():
    """Create a checkout in /srv with correct ownership."""
    info = _Info()
    if exists(BASEDIR):
        if not confirm(
            "Directory %s already exists. Really set it up anew?" % BASEDIR,
            default=False):
            return
    # Create a directory in /srv named after the hostname.
    sudo('mkdir -p %s' % BASEDIR)
    # Make buildout the owner.
    sudo('chown buildout:buildout %s' % BASEDIR)
    # And make a checkout of the latest tag *as user buildout*.
    sudo(info.initial_checkout_cmd(), user='buildout')


def initial_create_database():
    """Create database and/or db user."""
    if confirm("Create user %s on %s?" % (DB_USER, DB_HOST),
               default=False):
        local('createuser -h {host} -U postgres --pwprompt {user}'.format(
                host=DB_HOST, user=DB_USER))
    if confirm("Create database %s on %s with template postgis?" % (
            DB_NAME, DB_HOST), default=True):
        cmd = ('createdb -h {host} -U postgres --template=template_postgis ' +
               '--owner={user} {database}')
        local(cmd.format(host=DB_HOST, user=DB_USER, database=DB_NAME))


def initial_switch_and_start():
    """Just runs regular_switch_and_restart()."""
    regular_switch_and_restart()


def initial_nginx_symlinks():
    """Make nginx symlinks into /etc as root."""
    # Find nginx configs.
    configs = [filename for filename in os.listdir('etc/')
               if filename.endswith('.nginx.conf')]
    for config in configs:
        source = os.path.join(BASEDIR, 'etc', config)
        target_available = os.path.join('/etc/nginx/sites-available/', config)
        target_enabled = os.path.join('/etc/nginx/sites-enabled/', config)
        if exists(target_available):
            print("%s already exists." % target_available)
        else:
            sudo("ln -s %s %s" % (source, target_available))
        if exists(target_enabled):
            print("%s already exists." % target_enabled)
        else:
            sudo("ln -s %s %s" % (target_available, target_enabled))
    if confirm("Reload nginx config?", default=True):
        sudo("/etc/init.d/nginx reload")


def initial_symlink_django_logrotate():
    """Install the logrotate script for this site's django.log."""
    configs = [filename for filename in os.listdir('etc/')
               if filename.endswith('.logrotate')]
    for config in configs:
        source = os.path.join(BASEDIR, 'etc', config)
        target = os.path.join('/etc/logrotate.d/', config)
        if exists(target):
            sudo("rm %s" % target)
        sudo("ln -s %s %s" % (source, target))


def regular_switch_and_restart():
    info = _Info()
    if not exists(BASEDIR):
        abort(
            "Directory %s doesn't exist yet. Run 'create_srv_dir'." % BASEDIR)
    with cd(BASEDIR):
        if not confirm("Switch to tag %s on %s?" % (
                info.last_tag, env['host']), default=True):
            abort("Aborted.")
        if info.svn:
            tag_url = info.vcs.tag_url(info.last_tag)
            print("Switching to %s" % tag_url)
            sudo("svn switch %s" % tag_url, user='buildout')
        if info.git:
            sudo("git fetch", user='buildout')
            sudo("git checkout %s" % info.last_tag, user='buildout')
        if not exists(os.path.join(BASEDIR, 'buildout.cfg')):
            print("buildout.cfg doesn't exist yet.")
            print("You should symlink one of the others:")
            sudo("ls -l *.cfg", user='buildout')
            cfg = prompt("Name of the cfg to symlink:")
            cfg_file = os.path.join(BASEDIR, cfg)
            if not exists(cfg_file):
                abort("%s doesn't exist!" % cfg_file)
            sudo("ln -s %s buildout.cfg" % cfg_file, user='buildout')
        check_is_symlink = ("python -c \"import os;" +
                            "print(os.path.islink('buildout.cfg'))\"")
        if 'False' in sudo(check_is_symlink, user='buildout'):
            abort("buildout.cfg isn't a symlink.")
        if not exists(os.path.join(BASEDIR, 'bin', 'buildout')):
            print("bin/buildout doesn't exist yet. Running bootstrap.")
            sudo("python bootstrap.py -d", user='buildout')
        sudo("bin/buildout", user='buildout')
        if confirm("Sync and migrate the database?", default=True):
            sudo("bin/django syncdb", user='buildout')
            sudo("bin/django migrate", user='buildout')
        output = sudo("bin/supervisorctl status gunicorn", user='buildout')
        if 'refused' in output:
            print("Supervisor not running yet, starting it.")
            sudo("bin/supervisord", user='buildout')
        else:
            print("Restarting gunicorn...")
            sudo("bin/supervisorctl restart gunicorn", user='buildout')

