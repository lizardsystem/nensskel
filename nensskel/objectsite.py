# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.

import sys

from paste.script import templates

# Bloody hack for cheetah
reload(sys)
sys.setdefaultencoding('UTF-8')


class ObjectSite(templates.Template):
    _template_dir = 'templates/objectsite'
    summary = "A buildout for nens object django sites"
    required_templates = ['nens_library']
    use_cheetah = True
