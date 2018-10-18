plonecli
========

plonecli_ is a helper to for developing Plone packages and helps using mr.bob based templates present on `bobtemplates.plone`_.

The templates provided by us at bobtemplates.cs are also available on plonecli, so you can use them easily:

.. code-block:: shell

   $ pip install plonecli
   $ plonecli --list-templates
    Available mr.bob templates:
    - theme_package
    - buildout
    - addon
    - view
    - vocabulary
    - content_type
    - viewlet
    - behavior
    - theme_barceloneta
    - portlet
    - theme
    - cs_plone_buildout


And use it:

.. code-block:: shell

   $ plonecli create cs_plone_buildout myproject



.. _plonecli: https://pypi.org/project/plonecli/
.. _`bobtemplates.plone`: https://pypi.org/project/bobtemplates.plone/
