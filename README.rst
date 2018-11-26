
.. image:: https://secure.travis-ci.org/codesyntax/bobtemplates.cs.png?branch=master
    :target: http://travis-ci.org/codesyntax/bobtemplates.cs

.. image:: https://coveralls.io/repos/github/codesyntax/bobtemplates.cs/badge.svg?branch=master
    :target: https://coveralls.io/github/codesyntax/bobtemplates.cs?branch=master
    :alt: Coveralls

.. image:: https://img.shields.io/pypi/v/bobtemplates.cs.svg
    :target: https://pypi.python.org/pypi/bobtemplates.cs/
    :alt: Latest Version

.. image:: https://readthedocs.org/projects/bobtemplatescs/badge/?version=latest
        :target: https://bobtemplatescs.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://img.shields.io/pypi/l/bobtemplates.cs.svg
    :target: https://pypi.python.org/pypi/bobtemplates.cs/
    :alt: License

================
bobtemplates.cs
================

`bobtemplates.cs` provides a `mr.bob <http://mrbob.readthedocs.org/en/latest/>`_ template to generate packages for Plone projects using our customizations. This packages is based on `bobtemplates.plone <https://pypi.python.org/project/bobtemplates.plone>`_


Features
========

Package created with ``bobtemplates.cs`` use the current best-practices when creating an add-on.

Provided templates
------------------

- cs_plone_buildout
- cs_migration

cs_plone_buildout
~~~~~~~~~~~~~~~~~

This template provides a ready-to-use buildout template for Plone sites. It asks for a Plone version
and configures the buildout with it.

The generated buildout provides configuration files for nginx and Apache, haproxy, varnish and logrotate.

It also creates cron jobs to pack your database and to restart the services when the server is rebooted.


cs_migration
~~~~~~~~~~~~

This template adds some useful blueprints and a pipeline for a `Transmogrifier`_ based migration for Plone 5.

The provided pipeline will work with a
`collective.jsonify <https://pypi.org/project/collective.jsonify/>`_ export out of the box.

We have been using the blueprints and the pipeline in several projects and found them very useful. To make the pipeline work correctly, you will need to adjust the created migration1.cfg file to provide the path of the export and adjust one or two parameters.

To get started with Transmogrifier, visit the training at https://training.plone.org/5/transmogrifier

You can run the migration from the command line, using the provided zopectl scripts, as follows. Inspect all the registered transmogrifier pipelines::

  $ cd /path/to/your/buildout
  $ ./bin/instance list_migrations


Run the selected pipeline::

  $ cd /path/to/your/buildout
  $ ./bin/instance run_migration my.package-step1




Compatibility
=============

Add-ons created with ``bobtemplates.cs`` are tested to work in Plone 5 and Plone 5.1.
They should also work with older versions but that was not tested.
It should work on Linux, Mac and Windows.


Documentation
=============

Full documentation for end users can be found in the "docs" folder.


Contribute
==========

- Issue Tracker: https://github.com/codesyntax/bobtemplates.cs/issues
- Source Code: https://github.com/codesyntax/bobtemplates.cs
- Documentation:


Support
=======

If you are having issues, please let us know.

.. _`Transmogrifier`: https://pypi.org/projects/collective.transmogrifier
