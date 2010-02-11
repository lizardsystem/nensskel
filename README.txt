Paster skeletons for Nelen & Schuurmans
=======================================

``nensskel`` provides so-called "paster templates" for easy creation of new
lizard websites, libraries and so on.

The nensskel script creates a directory structure with lots of basic files
(like a readme and a setup.py) already there and partially filled in.
Optionally it also creates a trunk/tags/branches structure in svn for you.

Just call the nensskel script to get usage information.


Installation can be done as a development installation or by a simple::

    $> easy_install -i http://lizardpackages.vanrees.org nensskel


Development installation
------------------------

Do the regular ``python bootstrap.py && bin/buildout`` and you're set up.  The
nensskel and paster script are created in the bin/ directory.

There's one python script in ``nensskel/*.py`` per template.  The actual
templates are in ``nensskel/templates/*``.  See
http://pythonpaste.org/script/developer.html for some limited documentation on
what paster can do.  If you want examples:
http://svn.plone.org/svn/collective/ZopeSkel/trunk/ is the most elaborate set
of templates available.

Run the tests with ``bin/test`` and don't forget to look at the buildbot after
you made changes as it is particularly easy to make only-works-locally
mistakes when working on paster templates.
