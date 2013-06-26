import os
import shutil
import tempfile
import unittest


class TestObjectSite(unittest.TestCase):
    def setUp(self):
        self.cwd = os.getcwd()
        self.tempdir = tempfile.mkdtemp()
        os.chdir(self.tempdir)

    def tearDown(self):
        shutil.rmtree(self.tempdir)
        os.chdir(self.cwd)

    def test_run(self):
        """Check code from run."""
        assert(True)

    def test_created_files(self):
        """Check if all the necessary files are created."""
        import paste.script.command
        args = ['create', 'testsite', '-t', 'nens_objectsite']
        paste.script.command.run(args)

        paste_dir = os.path.join(self.tempdir, 'testsite')

        dir_contents = ['.coveragerc',
                        '.gitignore',
                        '.tx',
                        'CHANGES.rst',
                        'CREDITS.rst',
                        'LICENSE.rst',
                        'MANIFEST.in',
                        'README.rst',
                        'bootstrap.py',
                        'development.cfg',
                        'doc',
                        'etc',
                        'fabfile.cfg',
                        'fabfile.py',
                        'nieuwegein',
                        'production.cfg',
                        'server.cfg',
                        'setup.cfg',
                        'setup.py',
                        'staging.cfg']
        self.assertEquals(os.listdir(paste_dir), dir_contents)
