# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
import sys
import pkginfo

from paste.script import templates

# Bloody hack for cheetah
reload(sys)
sys.setdefaultencoding('UTF-8')


class Objectsite(templates.Template):
    _template_dir = 'templates/objectsite'
    summary = "A buildout for nens object django sites"
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
        vars['nensskel_version'] = pkginfo.Installed('nensskel').version
        vars['github_organization'] = 'nens'
        templates.Template.run(self, command, output_dir, vars)
