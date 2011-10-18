# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
import os
import subprocess


def svn_propset(directory, ignores, setting='svn:ignore'):
    """If the directory is an svn dir, add ignores to svn:ignores"""
    if not os.path.exists(os.path.join(directory, '.svn')):
        # No svn dir, so we won't set anything.
        # This also applies if the dir doesn't even exists.
        return
    to_ignore = '\n'.join(ignores)
    # TODO: check if this works on windows.
    subprocess.call(['svn', 'propset', setting, to_ignore, directory])


def print_egginfo_removal_instructions(output_dir, vars, extra_reverts=None):
    """Print egg-info removal instructions."""
    if extra_reverts is None:
        extra_reverts = []
    using_svn = os.path.exists(os.path.join(output_dir, '.svn'))

    egginfo_dirname = '%(package)s.egg-info' % vars
    print
    print "Manual task that you need to do:"
    print "cd %s" % output_dir
    if using_svn:
        print "svn revert %s" % egginfo_dirname
        for extra_revert in extra_reverts:
            print "svn revert %s" % extra_revert
    print "rm -rf %s" % egginfo_dirname
    print
