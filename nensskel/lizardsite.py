# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
import os
import uuid
import sys

from paste.script import templates

from nensskel import utils

# Bloody hack for cheetah
reload(sys)
sys.setdefaultencoding('UTF-8')


class Lizardsite(templates.Template):
    _template_dir = 'templates/lizardsite'
    summary = "A buildout for nens lizard django sites"
    required_templates = ['nens_djangoapp']
    use_cheetah = True

    def run(self, command, output_dir, vars):
        vars['secret_key'] = uuid.uuid4()
        templates.Template.run(self, command, output_dir, vars)

    def post(self, command, output_dir, vars):
        testsettings = os.path.join(output_dir, vars['package'],
                                    'testsettings.py')
        os.remove(testsettings)
        testsettings_location = os.path.join(vars['package'],
                                             'testsettings.py')
        os.remove(os.path.join(output_dir, 'buildout.cfg'))
        utils.print_egginfo_removal_instructions(
            output_dir,
            vars,
            extra_reverts=[testsettings_location])
