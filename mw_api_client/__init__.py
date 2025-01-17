"""
A really simple MediaWiki API client.

Can use most MediaWiki API modules.

Requires the ``requests`` library.

http://www.mediawiki.org/

Installation
============

To install the latest stable version::

    pip install -U mw-api-client

To install the latest development (likely unstable) version::

    git clone https://github.com/Kenny2github/mw-api-client.git
    cd mw-api-client
    python setup.py install

Example Usage
=============

.. code-block:: python

    import mw_api_client as mw

Get a page:

.. code-block:: python

    wp = mw.Wiki("https://en.wikipedia.org/w/api.php", "MyCoolBot/0.0.0")

    wp.login("kenny2wiki", password)

    sandbox = wp.page("User:Kenny2wiki/sandbox")

Edit page:

.. code-block:: python

    # Get the page
    contents = sandbox.read()

    # Change
    contents += "\n This is a test!"
    summary = "Made a test edit"

    # Submit
    sandbox.edit(contents, summary)

List pages in category:

.. code-block:: python

    for page in wp.category("Redirects").categorymembers():
        print(page.title)

Remove all uses of a template:

.. code-block:: python

    stub = wp.template("Stub")

    # Pages that transclude stub, main namespace only
    target_pages = list(stub.transclusions(namespace=0))

    # Sort by title because it's prettier that way
    target_pages.sort(key=lambda p: p.title)

    for page in target_pages:
        page.replace("{{stub}}", "")

Patrol all recent changes in the Help namespace:

.. code-block:: python

    rcs = wp.recentchanges(rcnamespace=12)

    for rc in rcs:
        rc.patrol()


Made by Kenny2github, based off of ~blob8108's Scratch Wiki API client.

MIT Licensed.
"""
from __future__ import print_function

GETINFO = False #pylint: disable=wrong-import-position

from .wiki import Wiki
from .page import Page, User, Revision, CurrentUser
from .excs import WikiError, WikiWarning, EditConflict, catch
from .misc import Tag, RecentChange, GenericData
from .qyoo import Queue

__version__ = '3.2.0'

__all__ = [
    'EditConflict',
    'GETINFO',
    'Page',
    'Queue',
    'RecentChange',
    'Revision',
    'Tag',
    'User',
    'CurrentUser',
    'Wiki',
    'WikiError',
    'WikiWarning',
    'catch'
]
