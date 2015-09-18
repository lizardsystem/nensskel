Just a burn test: create projects out of the templates and run buildout on
them.

The test setup prepares a temporary directory that is thrown away in the
teardown method:

    >>> import os
    >>> from pprint import pprint
    >>> os.listdir(tmp)
    []

Find paster:

    >>> curdir = os.getcwd()
    >>> paster = os.path.join(curdir, 'bin', 'paster')
    >>> os.path.exists(paster)
    True

List the templates:

    >>> print 'start', system(paster + ' create --list-templates') #doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
    start ...
    nens_library:
    ...

Do the smoke tests:

    >>> os.chdir(tmp)
    >>> dont_care = system(paster + ' create -t nens_library aaa')
    >>> contents = sorted(os.listdir(os.path.join(tmp, 'aaa')))
    >>> if 'aaa.egg-info' in contents:
    ...     # Compensate for distribute/setuptools difference.
    ...     contents.remove('aaa.egg-info')
    >>> pprint(contents)
    ['.coveragerc',
     '.gitignore',
     'CHANGES.rst',
     'CREDITS.rst',
     'LICENSE.rst',
     'MANIFEST.in',
     'README.rst',
     'aaa',
     'bootstrap.py',
     'buildout.cfg',
     'doc',
     'setup.cfg',
     'setup.py']

    >>> dont_care = system(paster + ' create -t nens_djangoapp li-zard')
    >>> contents = sorted(os.listdir(os.path.join(tmp, 'li-zard')))
    >>> if 'li_zard.egg-info' in contents:
    ...     # Compensate for distribute/setuptools difference.
    ...     contents.remove('li_zard.egg-info')
    >>> pprint(contents)
    ['.coveragerc',
     '.gitignore',
     '.tx',
     'CHANGES.rst',
     'CREDITS.rst',
     'LICENSE.rst',
     'MANIFEST.in',
     'README.rst',
     'bootstrap.py',
     'bower.json',
     'buildout.cfg',
     'doc',
     'li_zard',
     'setup.cfg',
     'setup.py']

    >>> dont_care = system(paster + ' create -t nens_lizardsite nieuwegein')
    >>> contents = sorted(os.listdir(os.path.join(tmp, 'nieuwegein')))
    >>> if 'nieuwegein.egg-info' in contents:
    ...     # Compensate for distribute/setuptools difference.
    ...     contents.remove('nieuwegein.egg-info')
    >>> pprint(contents)
    ['.coveragerc',
     '.gitignore',
     '.tx',
     'CHANGES.rst',
     'CREDITS.rst',
     'LICENSE.rst',
     'MANIFEST.in',
     'README.rst',
     'bootstrap.py',
     'bower.json',
     'development.cfg',
     'doc',
     'etc',
     'fabfile.cfg',
     'fabfile.py',
     'nieuwegein',
     'production.cfg',
     'server.cfg',
     'setup.cfg',
     'setup.py',
     'staging.cfg']
    >>> subdir_contents = sorted(os.listdir(
    ...     os.path.join(tmp, 'nieuwegein', 'nieuwegein')))
    >>> settings = [item for item in subdir_contents if 'settings' in item]
    >>> pprint(settings)
    ['developmentsettings.py', 'settings.py', 'stagingsettings.py']

And now for some serious buildout running. This is the best we can do to
verify everything mostly works. We cannot run ``bin/test`` in them afterwards
as not all data is filled in yet.

The python library:

    >>> os.chdir(os.path.join(tmp, 'aaa'))
    >>> print 'start', system('python bootstrap.py') #doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
    start...
    Creating directory .../aaa/bin'.
    ...
    Generated script .../aaa/bin/buildout...
    >>> print 'start', system('bin/buildout') #doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
    start...
    Installing sphinx.
    ...

(We test for sphinx as that's the last part being installed).

The lizard app:

    >>> os.chdir(os.path.join(tmp, 'li-zard'))
    >>> print 'start', system('python bootstrap.py') #doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
    start...
    Creating directory .../li-zard/bin'.
    ...
    Generated script .../li-zard/bin/buildout...
    >>> print 'start', system('bin/buildout') #doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
    start...
    Installing sphinx.
    ...

The lizard site:

    >>> os.chdir(os.path.join(tmp, 'nieuwegein'))
    >>> dont_care = system("ln -s development.cfg buildout.cfg")
    >>> print 'start', system('python bootstrap.py') #doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
    start...
    Creating directory .../nieuwegein/bin'.
    ...
    Generated script .../nieuwegein/bin/buildout...
    >>> print 'start', system('bin/buildout') #doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
    start...
    Installing sphinx.
    ...
