# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.

import sys
import pkginfo
import random

from paste.script import templates

from nensskel import utils

# Bloody hack for cheetah
reload(sys)
sys.setdefaultencoding('UTF-8')

CHARS = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'


class Leansite(templates.Template):
    _template_dir = 'templates/leansite'
    summary = "A buildout for nens lean django sites"
    use_cheetah = True

    def run(self, command, output_dir, vars):
        secret = ''.join([random.choice(CHARS) for i in range(50)])
        db_password1 = ''.join([random.choice(CHARS) for i in range(10)])
        db_password2 = ''.join([random.choice(CHARS) for i in range(10)])
        project = vars['project']
        if '_' in project:
            print "There's an underscore in the project name."
            print "Please use a dash instead."
            sys.exit(1)
        package = project
        if '-' in project:
            package = project.replace('-', '_')
            print "Project is called %s, the package will be %s" % (
                project, package)
        vars['package'] = package
        vars['secret_key'] = secret
        vars['nensskel_version'] = pkginfo.Installed('nensskel').version
        vars['github_organization'] = 'nens'
        vars['production_db_password'] = db_password1
        vars['staging_db_password'] = db_password2
        templates.Template.run(self, command, output_dir, vars)

    def post(self, command, output_dir, vars):
        utils.print_egginfo_removal_instructions(output_dir, vars)
