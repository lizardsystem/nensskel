# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
import sys

from paste.script import templates

from nensskel import utils

# Bloody hack for cheetah
reload(sys)
sys.setdefaultencoding('UTF-8')


class Djangoapp(templates.Template):
    _template_dir = 'templates/djangoapp'
    summary = "A buildout for nens django applications"
    required_templates = ['nens_library']
    use_cheetah = True

    def post(self, command, output_dir, vars):
        utils.print_egginfo_removal_instructions(output_dir, vars)
