# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
# Base Django settings.

import os

# SETTINGS_DIR allows media paths and so to be relative to this settings file
# instead of hardcoded to c:\only\on\my\computer.
SETTINGS_DIR = os.path.dirname(os.path.realpath(__file__))

# BUILDOUT_DIR is for access to the "surrounding" buildout, for instance for
# BUILDOUT_DIR/var/static files to give django-staticfiles a proper place
# to place all collected static files.
BUILDOUT_DIR = os.path.abspath(os.path.join(SETTINGS_DIR, '..'))

ADMINS = ()
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'NAME': '${package}',
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
    }
}

# Almost always set to 1.  Django allows multiple sites in one database.
SITE_ID = 1

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name although not all
# choices may be available on all operating systems.  If running in a Windows
# environment this must be set to the same as your system time zone.
TIME_ZONE = 'Europe/Amsterdam'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'nl-NL'
# For runtime language switching.  Note: they're shown in reverse order in
# the interface!
LANGUAGES = (
    ('nl', 'Nederlands'),
)
# If you set this to False, Django will make some optimizations so as not to
# load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds user-uploaded media.
MEDIA_ROOT = os.path.join(BUILDOUT_DIR, 'var', 'media')
# Absolute path to the directory where django-staticfiles'
# "bin/django build_static" places all collected static files from all
# applications' /media directory.
STATIC_ROOT = os.path.join(BUILDOUT_DIR, 'var', 'static')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
MEDIA_URL = '/media/'
# URL for the per-application /media static files collected by
# django-staticfiles.  Use it in templates like
# "{{ MEDIA_URL }}mypackage/my.css".
STATIC_URL = '/static_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '${secret_key}'

ROOT_URLCONF = '${package}.urls'

CACHES = {
    'default': {
        'KEY_PREFIX': BUILDOUT_DIR,
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

MIDDLEWARE_CLASSES = (
    # Gzip needs to be at the top.
    'django.middleware.gzip.GZipMiddleware',
    # Below is the default list, don't modify it.
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Lizard security.
    'tls.TLSRequestMiddleware',
    'lizard_security.middleware.SecurityMiddleware',
)

INSTALLED_APPS = (
    '${package}',
    'south',
    'compressor',
    'django_extensions',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.gis',
    'django.contrib.sessions',
    'django.contrib.sites',
)
