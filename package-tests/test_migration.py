# -*- coding: utf-8 -*-
from bobtemplates.cs import migration
from mrbob.configurator import Configurator

import os


def test_prepare_renderer():
    configurator = Configurator(
        template='bobtemplates.cs:cs_migration', target_directory='.'
    )
    assert configurator
    migration.prepare_renderer(configurator)


def test_post_renderer(tmpdir):
    target_path = tmpdir.strpath + '/collective.foo'
    package_path = target_path + '/src/collective/foo'
    os.makedirs(target_path)
    os.makedirs(package_path)

    template = """
    dummy
    '-*- Extra requirements: -*-'
    """
    with open(os.path.join(target_path + '/setup.py'), 'w') as f:
        f.write(template)

    template = """
    <configure
    xmlns="http://namespaces.zope.org/zope"
    xmlns:genericsetup="http://namespaces.zope.org/genericsetup"
    xmlns:i18n="http://namespaces.zope.org/i18n"
    xmlns:plone="http://namespaces.plone.org/plone">
    <!-- -*- extra stuff goes here -*- -->
    </configure>
    """
    with open(os.path.join(package_path + '/configure.zcml'), 'w') as f:
        f.write(template)

    configurator = Configurator(
        template='bobtemplates.cs:cs_migration',
        target_directory=package_path,
        bobconfig={'non_interactive': True},
    )
    migration.prepare_renderer(configurator)

    configurator.render()
    migration.post_renderer(configurator)
