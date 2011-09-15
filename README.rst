Django code skeletons
=====================

``nensskel`` provides so-called "paster templates" for easy creation of new
django applications, websites and python libraries.  They're not fully
generic, as they originate within one company.  See the note further down.

The nensskel script creates a directory structure with lots of basic files
(like a readme and a setup.py) already there and partially filled in.
Optionally it also creates a trunk/tags/branches structure in svn for you.

Just call the nensskel script to get usage information.

Installation can be done with pip or easy_install::

    $> easy_install nensskel

(Probably you need to run it with sudo on osx/linux).

Don't forget to update from time to time::

    $> easy_install --upgrade nensskel


Company-centricity
------------------

Nensskel originates at `Nelen & Schuurmans <http://www.nelen-schuurmans.nl>`_,
so we've of course set it up just the way we like it.  And we change it the
way we like it.

It does, however, give you a good example for full django applications/sites
with a complete setup.  For example, the django sites come with a full-blown
apache config.  And django-staticfiles is included for the easy css/js setup.


Example for your own skeleton
-----------------------------

When you want to create your own skeleton, nensskel can be a nice, small
example.  Just download the .tar.gz and unpack it.

Do the regular ``python bootstrap.py && bin/buildout`` and you're set up.  The
nensskel and paster script are created in the bin/ directory.

There's one python script in ``nensskel/*.py`` per template.  The actual
templates are in ``nensskel/templates/*``.  See
http://pythonpaste.org/script/developer.html for some limited documentation on
what paster can do.  If you want more elaborate examples:
http://svn.plone.org/svn/collective/ZopeSkel/trunk/ is the most elaborate set
of templates available.


Development and issue tracker
-----------------------------

Nensskel is developed on github: https://github.com/lizardsystem/nensskel .

The issue tracker is there, too:
https://github.com/lizardsystem/nensskel/issues .
