# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from sitesetup.fab.config import init_file
from sitesetup.fab.tasks import *

# Most settings can be configured in fabfile.cfg
init_file('fabfile.cfg')
