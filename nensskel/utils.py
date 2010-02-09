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
