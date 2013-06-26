Django code skeletons
=====================

``nensskel`` provides so-called "paster templates" for easy creation of new
django applications, websites and python libraries.  They're not fully
generic, as they originate within one company (see below).

The nensskel script creates a directory structure with (some partially filled) 
basic files (like a *README.rst* and a *setup.py*). Optionally it can create 
a trunk/tags/branches structure in svn.

.. image:: https://secure.travis-ci.org/lizardsystem/nensskel.png?branch=master
   :target: http://travis-ci.org/#!/lizardsystem/nensskel

Call the nensskel script to get usage information.

Install with pip or easy_install::

    $ easy_install nensskel

(Probably you need to run it with sudo on osx/linux).

Update for new versions::

    $ easy_install --upgrade nensskel

Available templates
-------------------

* **basic_package:**    A basic setuptools-enabled package
* **nens_djangoapp:**   A buildout for nens django applications
* **nens_library:**     A buildout for nens libraries
* **nens_lizardsite:**  A buildout for nens lizard django sites
* **nens_objectsite:**  A buildout for nens django sites
* **paste_deploy:**     A web application deployed through paste.deploy


Company-centricity
------------------

Nensskel originates at `Nelen & Schuurmans <http://www.nelen-schuurmans.nl>`_.
We set it up the way we like it and we change it the way we like it.

It does, however, provide a good example for full django applications/sites,
with a complete setup. For example, the django sites come with a full-blown
nginx config. Django-staticfiles is included for easy css/js setup.


Example for your own skeleton
-----------------------------

When you want to create your own skeleton, nensskel can be a nice, small
example.  Just download the .tar.gz and unpack it.

Do the regular ``python bootstrap.py && bin/buildout`` and you're good to go. 
The nensskel and paster scripts are created in the *bin/* directory.

There is one python script in ``nensskel/*.py`` per template.  The actual
templates are in ``nensskel/templates/*``.  See
http://pythonpaste.org/script/developer.html for some documentation on
what paster can do.  If you want elaborate examples:
http://svn.plone.org/svn/collective/ZopeSkel/trunk/ is the most elaborate set
of templates available.


Development and issue tracker
-----------------------------

Nensskel is developed on github: https://github.com/lizardsystem/nensskel .

Issues are also tracked there: https://github.com/lizardsystem/nensskel/issues .
