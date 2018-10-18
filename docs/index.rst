Introduction
============

..  toctree::
    :maxdepth: 1

``bobtemplates.cs`` provides a `mr.bob <http://mrbob.readthedocs.org/en/latest/>`_ template to generate a buildout package for Plone projects.

Installation
------------

Use in a buildout
^^^^^^^^^^^^^^^^^

::

    [buildout]
    parts += mrbob

    [mrbob]
    recipe = zc.recipe.egg
    eggs =
        mr.bob
        bobtemplates.cs


This creates a mrbob-executable in your bin-directory.
Call it from the ``src``-directory of your Plone project like this.

.. code-block:: shell

    ../bin/mrbob -O collective.foo bobtemplates:cs_plone_buildout


Installation in a virtualenv
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can also install ``bobtemplates.cs`` in a virtualenv.

.. code-block:: shell

    pip install bobtemplates.cs

With ``pip 6.0`` or newer ``mr.bob`` will automatically be installed as a dependency. If you still use a older version of pip you need install ``mr.bob`` before ``bobtemplates.cs``.

.. code-block:: shell

    pip install mr.bob

Now you can use it like this

.. code-block:: shell

    mrbob -O collective.foo bobtemplates:cs_plone_buildout

See `mr.bob <http://mrbob.readthedocs.org/en/latest/>`_ documentation for further information.


.. include:: intro.rst

.. include:: plonecli.rst

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
