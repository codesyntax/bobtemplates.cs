
.. image:: https://secure.travis-ci.org/plone/bobtemplates.cs.png?branch=master
    :target: http://travis-ci.org/plone/bobtemplates.cs

.. image:: https://coveralls.io/repos/github/plone/bobtemplates.cs/badge.svg?branch=master
    :target: https://coveralls.io/github/plone/bobtemplates.cs?branch=master
    :alt: Coveralls

.. image:: https://img.shields.io/pypi/dm/bobtemplates.cs.svg
    :target: https://pypi.python.org/pypi/bobtemplates.cs/
    :alt: Downloads

.. image:: https://img.shields.io/pypi/v/bobtemplates.cs.svg
    :target: https://pypi.python.org/pypi/bobtemplates.cs/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/status/bobtemplates.cs.svg
    :target: https://pypi.python.org/pypi/bobtemplates.cs/
    :alt: Egg Status

.. image:: https://img.shields.io/pypi/l/bobtemplates.cs.svg
    :target: https://pypi.python.org/pypi/bobtemplates.cs/
    :alt: License

.. image:: https://badges.gitter.im/plone/bobtemplates.cs.svg
    :target: https://gitter.im/plone/bobtemplates.cs?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge
    :alt: Gitter channel

==================
bobtemplates.cs
==================

``bobtemplates.cs`` provides a `mr.bob <http://mrbob.readthedocs.org/en/latest/>`_ template to generate packages for Plone projects using our customizations. This packages is based on `bobtemplates.plone <https://pypi.python.org/project/bobtemplates.plone`


Features
========

Package created with ``bobtemplates.cs`` use the current best-practices when creating an add-on.

Provided templates
------------------

- buildout



Compatibility
=============

Add-ons created with ``bobtemplates.cs`` are tested to work in Plone 4.3.x and Plone 5.
They should also work with older versions but that was not tested.
It should work on Linux, Mac and Windows.


Documentation
=============

Full documentation for end users can be found in the "docs" folder.

Installation
============

Use in a buildout
-----------------

.. code-block:: ini

    [buildout]
    parts += mrbob

    [mrbob]
    recipe = zc.recipe.egg
    eggs =
        mr.bob
        bobtemplates.cs


This creates a mrbob-executable in your bin-directory.
Call it from the ``src``-directory of your Plone project like this.

.. code-block:: console

    ../bin/mrbob bobtemplates.cs:addon -O collective.foo


Installation in a virtualenv
----------------------------

You can also install ``bobtemplates.cs`` in a virtualenv.

.. code-block:: console

    pip install bobtemplates.cs

With ``pip 6.0`` or newer ``mr.bob`` will automatically be installed as a dependency.
If you still use a older version of pip you need install ``mr.bob`` before ``bobtemplates.cs``.

.. code-block:: console

    pip install mr.bob

Now you can use it like this

.. code-block:: console

    mrbob bobtemplates.cs:addon -O collective.foo



See `the documentation of mr.bob <http://mrbob.readthedocs.org/en/latest/>`_  for further information.


Contribute
==========

- Issue Tracker: https://github.com/codesyntax/bobtemplates.cs/issues
- Source Code: https://github.com/codesyntax/bobtemplates.cs
- Documentation:


Support
=======

If you are having issues, please let us know.
