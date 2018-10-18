# -*- coding: utf-8 -*-

from bobtemplates.cs import buildout
from mrbob.configurator import Configurator


def test_prepare_renderer():
    configurator = Configurator(
        template='bobtemplates.cs:cs_plone_buildout',
        target_directory='collective.foo',
        variables={'buildout_zope_port_number': '8080'},
    )
    buildout.prepare_renderer(configurator)
    assert configurator.variables['template_id'] == 'cs_plone_buildout'


def test_post_renderer():
    buildout.post_renderer(None)
