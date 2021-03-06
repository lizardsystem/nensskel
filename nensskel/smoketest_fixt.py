# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
"""Fixture for the smoketest.txt doctest"""

import os
import shutil
import subprocess
import sys
import tempfile

MUST_CLOSE_FDS = not sys.platform.startswith('win')


def system(command, input=''):
    """commands.getoutput() replacement that also works on windows"""
    p = subprocess.Popen(command,
                         shell=True,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         close_fds=MUST_CLOSE_FDS)
    i, o, e = (p.stdin, p.stdout, p.stderr)
    if input:
        i.write(input)
    i.close()
    result = o.read() + e.read()
    o.close()
    e.close()
    return result


def setup_test(test):
    """Prepare an empty directory"""
    test.original_dir = os.getcwd()
    test.tempdir = tempfile.mkdtemp()
    test.globs['tmp'] = test.tempdir
    test.globs['system'] = system


def teardown_test(test):
    """Clean up the temp directory"""
    shutil.rmtree(test.tempdir)
    os.chdir(test.original_dir)
