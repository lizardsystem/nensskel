# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.

from .base import *

DATABASES = {
    'default': {
        'USER': '${package}',
        'PASSWORD': '${production_db_password}',
    }
}

# TODO: add production gauges ID here.
GAUGES_SITE_ID = ''
