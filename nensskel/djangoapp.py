import sys

from paste.script import templates

# Bloody hack for cheetah
reload(sys)
sys.setdefaultencoding('UTF-8')


class Djangoapp(templates.Template):
    _template_dir = 'templates/djangoapp'
    summary = "A buildout for nens django applications"
    required_templates = ['nens_library']
    use_cheetah = True
