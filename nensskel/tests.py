import os
import shutil
import tempfile
import unittest

import mock


class TestObjectSite(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.cwd = os.getcwd()
        self.tempdir = tempfile.mkdtemp()
        os.chdir(self.tempdir)

    def tearDown(self):
        shutil.rmtree(self.tempdir)
        os.chdir(self.cwd)

    def test_run(self):
        """Check code from run."""
        assert(True)

    @mock.patch('sys.exit')
    def test_created_files(self, sys_exit):
        """Check if all the necessary files are created."""
        import paste.script.command
        args = ['create', 'testsite', '-t', 'nens_objectsite']

        paste.script.command.run(args)

        paste_dir = os.path.join(self.tempdir, 'testsite')

        dir_contents = ['setup.py',
                        'SOURCES.txt',
                        'entry_points.txt',
                        'dependency_links.txt',
                        'top_level.txt',
                        'not-zip-safe',
                        'PKG-INFO',
                        'requires.txt',
                        'project.rst',
                        'index.rst',
                        'conf.py',
                        'code.rst',
                        'config',
                        '.coveragerc',
                        '.gitignore',
                        'README.rst',
                        'CHANGES.rst',
                        'CREDITS.rst',
                        'LICENSE.rst',
                        'MANIFEST.in',
                        'bootstrap.py',
                        'base.cfg',
                        'production.cfg',
                        'staging.cfg',
                        'development.cfg',
                        'base.py',
                        'production.py',
                        'staging.py',
                        'development.py']
        objectsitefiles = []
        for root, dirs, files in os.walk(paste_dir):
            for file in files:
                objectsitefiles.append(file)

        self.assertItemsEqual(objectsitefiles, dir_contents)
