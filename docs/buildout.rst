=============================
Create Plone buildout package
=============================

With this template you can create a Plone buildout, which often used as a project buildout. The project buildout then can contain all project related packages directly or as separate repositories.

.. code-block:: sh

    mrbob bobtemplates.plone:cs_plone_buildout -O my_project

This will ask you for a port in which the main instance will run and will create a buildout folder for you.

The created buildout configuration has the standards that we use at CodeSyntax to create our projects. It contains supervisor configuration and provides also templates to configure your Apache or nginx server.

Additionaly it has extra configuration if you want to build varnish and/or haproxy with buildout.

For a common buildout it creates two configuration files: buildout.cfg for standard development and deployment.cfg for deployment configuration (basically with debug-mode disabled)

To initialize the buildout, change into the buildout folder and use the following commands:

.. code-block:: sh

    virtualenv .
    ./bin/pip install -r requirements.txt
    ./bin/buildout
