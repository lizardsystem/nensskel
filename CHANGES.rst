Changelog for nensskel
======================


1.36 (2015-09-19)
-----------------

- Update packages mitigating the 'ValueError: too many values to unpack'.

- Updated versions, using new lizard5 KGS. You can just as well remove the
  'extends' line for your own projects, but at least for testing nensskel, I'm
  keeping it in for now.
  [reinout]

- Fixed djangorecipe setup. Deprecated options have been removed (fixes
  #12).
  [reinout]

- Using ``wsgi.py`` file and the new djangorecipe ``scripts-with-settings`
  option: this fixes the gunicorn (and celery) setup for modern
  django/gunicorn combinations.
  [reinout]

- Improved tests so that more buildout failures show up (like the necessary
  djangorecipe changes from the previous point). The test setup now also
  includes coverallls.io integration for coverage reports.
  [reinout]


1.35 (2015-01-21)
-----------------

- Unpinned buildout default version. Updated bootstrap.py.


1.34 (2014-10-06)
-----------------

- Updated everything for django 1.6 (regarding imports) and buildout 2.x.

- Added the new leansite template (also removed it again).

- Removed the deprecated GZipMiddleware from Django settings for all templates.


1.33 (2013-05-02)
-----------------

- Corrected sentry/raven setup.

- Prepare django apps and sites to be translatable with Transifex.


1.32 (2013-02-18)
-----------------

- Bugfix: there was still a ``buildout-versions`` in the lizardsite template.


1.31 (2013-02-15)
-----------------

- Upgraded nensskel's own setup to buildout 2.0.

- Updated nose/coverage test setup in the generated projects *and* in ourselves.

- Added pydev support also to lib/djangoapp buildouts instead of only to the
  site buildout.

- Updated lizardsite demo fixture to the latest lizard-wms.


1.30 (2013-02-11)
-----------------

- Added buildout 2.0!

- Added a django-session-cleanup-cronjob part for production and staging,
  which cleans old sessions in the database.

- Added nose coverage report setup. And included mock by default.

- Added ``__future__`` imports everywhere for print statements and unicode.
  Everywhere except django settings, btw, as that weirdly breaks the
  testrunner!


1.29 (2012-10-11)
-----------------

- The library buildout.cfg now also extends the latest KGS; this
  prevents problems with mismatched buildout versions.


1.28 (2012-10-11)
-----------------

- Fixed license header (small tweak only: it pointed to LICENSE.txt
  instead of the .rst one).

- Added max log size of 10MB to the logrotate script in the lizard
  site template.


1.27 (2012-09-24)
-----------------

- Added lizard-wms (and lizard-maptree) to the lizardsite template. Almost
  every site needs them and it makes the empty site more suited for demo
  purposes and experimenting.


1.26 (2012-06-28)
-----------------

- Fixed small issues in the lizardsite template:

  - Added ``auto-checkout`` plus explanation to its buildout config.

  - Generated random password for the production/staging databases.

  - Using site name as database name.


1.25 (2012-06-26)
-----------------

- Git instructions are now printed after generating the project (if we're not
  generating an svn project). It assumes nens/lizardsystem github URLs (which
  you can change, of course).

- Added more example imports to ``views.py`` and ``models.py``, for instance
  the ``ugettext``/``ugettext_lazy`` import. And the lizard-ui and lizard-map
  base class based views.

- Added example class based view configuration in ``urls.py``.

- Added ``admin.py``.

- Added the ``from __future__ import unicode_literals`` import to use unicode
  everywhere.

- Updated .gitignore: we now ignore the nginx config files instead of the
  not-used-anymore apache ones.


1.24 (2012-06-19)
-----------------

- Added nensskel version number to the generated 'initial generation'
  changelog entry.

- Removed TODO.rst from all the templates. We don't actually use it.

- Added configuration for testing `on travis
  <http://travis-ci.org/#!/lizardsystem/nensskel>`_.

- Using url() instead of tuples in the url patterns again. Plus fixed syntax
  error there.

- Updated lizardsite skeleton to latest server configuration and
  fabfile.

- Added stagingsettings.py, staging.cfg

- Made tests work


1.22 (2011-12-08)
-----------------

- Added a templates/ subdirectory to the djangoapp.

- Renamed media/ dir in djangoapp to static/ to match Django 1.3.


1.21 (2011-11-15)
-----------------

- Using latest and greatest server setup. Including nginx and sitesetup.


1.20 (2011-10-21)
-----------------

- Added MEDIA_URL and MEDIA_ROOT to the djangoapp template. The debugmode
  urlpatterns loaded in ``urls.py`` fail with a traceback otherwise.


1.19 (2011-10-18)
-----------------

- Updated the .coveragerc to be more complete.


1.18 (2011-10-18)
-----------------

- Not git-ignoring ``*.mo`` files by default: django doesn't compile them on
  the fly, so they need to be included with the source code.

- Using 'graft' option in the MANIFEST.in to just include everything in our
  project directory. .pyc/pyo files are excluded anyway, so this is more or
  less OK.


1.17 (2011-09-30)
-----------------

- Important bugfix: the "hidden" ``.something`` files weren't being
  generated. They *are* now.


1.16 (2011-09-09)
-----------------

- Added git ignore file and basic MANIFEST.in to the templates.

- Removed unneeded lizard-ui middleware as django 1.3's logging handles it.

- Adjusted context processors to django 1.3's default list.

- Added logging setup for sentry in the lizard site template.

- Cleaned up the urls.py from djangoapp.


1.15 (2011-08-25)
-----------------

- Added the KGS to djangoapp and sites and updated for django 1.3.

- Removed map_settings from lizardsite settings.py.

- Commented out wsgiimmportscript in apache conf (it gives an error).

- Added lizard-map context processor (outcommented) in lizardsite
  settings.py.


1.14 (2011-05-30)
-----------------

- Adding deadlock-timeout and especially display-name to the wsgi config. The
  deadlock might help with shapefiles clogging up the server. The display-name
  shows you which server is actually using up the CPU/mem instead of just
  showing 'apache2'.


1.13 (2011-05-23)
-----------------

- Re-release of 1.12 as that download tarball was broken.

- Adding django.contrib.gis to the ``INSTALLED_APPS`` lists as that's needed
  for south migrations of geo fields.

- nens_djangoapp's ``testsettings.py`` was missing an ``import os``.


1.12 (2011-04-13)
-----------------

- Modifying the middleware to include SentryResponseErrorIdMiddleware.


1.11 (2011-04-13)
-----------------

- Added django-sentry to the Lizardsite template.
- Adding new file setup.py_tmpl to Lizardsite template.
- Updating +package+/settings.py_tmpl which adds sentry to INSTALLED_APPS.


1.10 (2011-03-31)
-----------------

- Adding mostly-empty READMEs to the two empty 'fixtures' and
  'media/+package+' dirs in the django app template. On some machines, the
  empty directories were not getting created. This way they are.

- Svn-ignoring the ``doc/build`` directory (with sphinx output).

- Added ``svn revert`` instructions for ``testsettings.py`` in the website
  template (in addition to removing the file).


1.9 (2011-03-02)
----------------

- Small restructured text heading level fixes for the sphinx documentation.


1.8 (2011-02-01)
----------------

- Removed buildout usage part from the readme.rst as it gets repeated
  lots of times all over the place this way.

- Added matplotlib tweaks to the django site settings.py.

- Added django-extensions to the standard dependencies of django apps
  so that we can get a model graph.


1.7 (2011-01-19)
----------------

- Added sphinx setup.  Also swapped the .txt files for .rst ones.


1.6.1 (2010-12-03)
------------------

- Fixed too-restrictive regex in apache's openlayers AliasMatch: the
  openlayers css/icons now also work in the root of the site...


1.6 (2010-12-03)
----------------

- Added sysegg part to the buildouts.


1.5 (2010-12-03)
----------------

- Printing .egginfo directory removal instructions.

- Updated list of standard svn:ignores.

- Added django gzip middleware to the lizardsite template.

- Added lizard-ui's traceback logging middleware to lizardsite.

- Added lizard-map's map settings to the django settings.py in lizardsite.

- Removed windows apache configuration.

- Added gzip ("mod_deflate") for js/css in the apache config.

- Eternally caching the django-compressor combined js/css files.

- Added logging setup to lizardsite.

- Added 500.html and 404.html to lizardsite template.

- Added openlayers img/ and theme/ aliases to compensate for openlayers'
  weirdness.

- Added extra part to the lizardsite buildout for automatic ``bin/django
  build_static`` running so we won't ever forget to do that.

- Updated database settings to new django multiple databases style.


1.4 (2010-10-15)
----------------

- Added setup.cfg that tells nose to output xml test reports for use with
  Hudson.

- Fixes to the test setup of django_app.


1.3 (2010-10-01)
----------------

- Added copyright notice at the top of every file including pointer to the
  LICENSE.txt GPL file.  No, I'm not copy/pasting 10 unneeded lines of GPL
  boilerplate into every file.


1.2 (2010-08-25)
----------------

- Bootstrap.py adjustments: using the 1.4.x buildout one for now.


1.1.1 (2010-08-10)
------------------

- Documentation update.


1.1 (2010-08-10)
----------------

- Changed test setup of djangoapp and lizardsite to match Reinout's latest
  experiments :-)


1.0 (2010-08-03)
----------------

- Added coverage support both to nensskel itself and to the templates.


0.5 (2010-08-02)
----------------

- Added django compressor settings to the lizardsite template.

- Added lizard-ui as a standard dependency for django applications.


0.4 (2010-05-20)
----------------

- Removed ipython as it regularly fails to download, sadly.  Can be re-added
  after buildout gains a timeout setting (in the .cfg files).


0.3 (2010-03-22)
----------------

- Django STATIC_URL/MEDIA_URL clarification and usage improvement after
  discussion on http://bitbucket.org/jezdez/django-staticfiles/issue/12/

- Added apache config (with a separate one for windows that still needs some
  work).


0.2 (2010-02-12)
----------------

- Django fixes after using skeleton in real life.


0.1 (2010-02-11)
----------------

- Added ``nensskel`` script as a handy wrapper around ``paster create``.

- Added lizardsite skeleton (which needs checking and probably modifications).

- Added djangoapp skeleton.

- Added library skeleton.

- Added test that creates instances of all skeletons and runs their
  bin/buildout.  Smoke test: switch everything on and see if smoke comes out.

- Reinout copied relevant parts from the thaskel and zestskel that he made for
  the two previous companies he worked for.
