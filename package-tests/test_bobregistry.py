# -*- coding: utf-8 -*-

from bobtemplates.cs import bobregistry


def test_reg_cs_plone_buildout():
    reg = bobregistry.cs_plone_buildout()
    assert reg.template == u'bobtemplates.cs:cs_plone_buildout'
    assert reg.plonecli_alias == u'cs_plone_buildout'
    assert not reg.depend_on
    assert not reg.deprecated
    assert not reg.info
