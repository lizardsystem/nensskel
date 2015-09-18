Django code skeletons
=====================

.. image:: https://travis-ci.org/lizardsystem/nensskel.svg?branch=master
    :target: https://travis-ci.org/lizardsystem/nensskel


.. image:: https://coveralls.io/repos/lizardsystem/nensskel/badge.svg?branch=reinout-version-upgrades&service=github
  :target: https://coveralls.io/github/lizardsystem/nensskel?branch=reinout-version-upgrades



``nensskel`` provides so-called "paster templates" so you can easily create new
Django applications, websites and python libraries.  They're not fully
generic, as they originated within one company (see below).

The nensskel script creates a directory structure for you with (some
partially filled) basic files (like a ``README.rst`` and a ``setup.py``).

Call the nensskel script to get usage information.

Installation is straightforward with easy_install::

    $ easy_install nensskel

or with pip::

    $ pip install nensskel

(Probably you need to run it with sudo on osx/linux).

Don't forget to update from time to time::

    $ easy_install --upgrade nensskel


Available templates
-------------------

Three nens-specific templates are included:

* **nens_library:**     A buildout for nens libraries

* **nens_djangoapp:**   A buildout for nens Django applications

* **nens_lizardsite:**  A buildout for nens lizard Django sites


Company-centricity
------------------

Nensskel originates at `Nelen & Schuurmans <http://www.nelen-schuurmans.nl>`_.
We set it up the way we like it and we change it the way we like it so it might
not fit your case 100%.

But it does provide a good example to give you a head start with a completely
setup Django application/site. For example, the Django sites come with a
full-blown nginx config and Django-staticfiles is included for easy css/js setup.

If the available templates don't serve your need, you can do two things:

- Clone the repository and edit the template as you like; possibly submit a
  pull request

- Make your own template


Drop us a line if you need help.


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
