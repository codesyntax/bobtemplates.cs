# -*- coding: utf-8 -*-

from bobtemplates.cs import bobregistry


def test_reg_cs_plone_buildout():
    reg = bobregistry.cs_plone_buildout()
    assert reg.template == u'bobtemplates.cs:cs_plone_buildout'
    assert reg.plonecli_alias == u'cs_plone_buildout'
    assert not reg.depend_on
    assert not reg.deprecated
    assert not reg.info


def test_reg_cs_migration():
    reg = bobregistry.cs_migration()
    assert reg.template == u'bobtemplates.cs:cs_migration'
    assert reg.plonecli_alias == u'cs_migration'
    assert reg.depend_on == u'plone_addon'
    assert not reg.deprecated
    assert not reg.info
