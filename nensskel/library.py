import sys

from paste.script import templates

from nensskel import utils

# Bloody hack for cheetah
reload(sys)
sys.setdefaultencoding('UTF-8')


class Library(templates.Template):
    _template_dir = 'templates/library'
    summary = "A buildout for nens libraries"
    required_templates = []
    use_cheetah = True

    def run(self, command, output_dir, vars):
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
        templates.Template.run(self, command, output_dir, vars)

    def post(self, command, output_dir, vars):
        """Clean up the result"""
        egginfo_dirname = '%(package)s.egg-info' % vars
        utils.svn_propset(output_dir,
                          ['bin',
                           'develop-eggs',
                           'coverage',
                           'parts',
                           'eggs',
                           egginfo_dirname,
                           'var',
                           '.installed.cfg'])
