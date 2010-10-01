# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
"""Command line script as simpler wrapper around paster"""

import sys

import paste.script.command


USAGE = """'nensskel' is a small wrapper around the 'paster create' command.

Basic usage: nensskel PROJECTNAME -t TEMPLATENAME [--svn-repository=URL]

PROJECTNAME is something like 'lizard_report' or 'turtlescripts' (without the
quotes, of course).

TEMPLATENAME is something like 'nens_library'.

URL is something like 'https://office.nelen-schuurmans.nl/svn/Products/'.
Nensskel creates a PROJECTNAME directory in there with trunk/tags/branches
structure.

These are the available templates (ignore basic_package and paste_deploy):
"""


def main():
    """Show usage msg when called without args, call paster otherwise.

    This method is installed by setup.py as the ``nensskel`` console_script.

    """
    args = sys.argv[1:]
    if len(args) == 0:
        print USAGE
        paste.script.command.run(['create', '--list-templates'])
    else:
        # Pass everything along to ``paster create``.
        args[0:0] = ['create']
        paste.script.command.run(args)
