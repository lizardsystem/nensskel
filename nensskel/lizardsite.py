# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
import os
import random
import sys

from paste.script import templates

from nensskel import utils

# Bloody hack for cheetah
reload(sys)
sys.setdefaultencoding('UTF-8')

CHARS = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'


class Lizardsite(templates.Template):
    _template_dir = 'templates/lizardsite'
    summary = "A buildout for nens lizard django sites"
    required_templates = ['nens_djangoapp']
    use_cheetah = True

    def run(self, command, output_dir, vars):
        secret = ''.join([random.choice(CHARS) for i in range(50)])
        vars['secret_key'] = secret
        db_password1 = ''.join([random.choice(CHARS) for i in range(10)])
        db_password2 = ''.join([random.choice(CHARS) for i in range(10)])
        vars['production_db_password'] = db_password1
        vars['staging_db_password'] = db_password2

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
