import sys

from paste.script import templates

# Bloody hack for cheetah
reload(sys)
sys.setdefaultencoding('UTF-8')


class Lizardsite(templates.Template):
    _template_dir = 'templates/lizardsite'
    summary = "A buildout for nens lizard django sites"
    required_templates = ['nens_djangoapp']
    use_cheetah = True

    def post(self, command, output_dir, vars):
        # Zap testsettings.py
        pass

