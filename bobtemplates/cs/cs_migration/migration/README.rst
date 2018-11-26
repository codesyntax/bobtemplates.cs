Migration documentation
=======================

Here you will find some useful blueprints and a pipeline for a `Transmogrifier`_ based migration for Plone 5.

The provided pipeline will work with a
`collective.jsonify <https://pypi.org/project/collective.jsonify/>`_ export out of the box.

To make the pipeline work correctly, you will need to adjust the created migration1.cfg file to provide the path of the export and adjust one or two parameters.

To get started with Transmogrifier, visit the training at https://training.plone.org/5/transmogrifier

You can run the migration from the command line, using the provided zopectl scripts, as follows. Inspect all the registered transmogrifier pipelines::

  $ cd /path/to/your/buildout
  $ ./bin/instance list_migrations


Run the selected pipeline::

  $ cd /path/to/your/buildout
  $ ./bin/instance run_migration {{{package.dottedname}}}-step1
