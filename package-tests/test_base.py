# -*- coding: utf-8 -*-

from bobtemplates.cs import base
from mrbob.configurator import Configurator

import os


def test_set_global_vars(tmpdir):
    template = """
[main]
version=5.1
"""
    target_dir = tmpdir.strpath + '/collective.foo'
    os.mkdir(target_dir)
    with open(os.path.join(target_dir + '/bobtemplate.cfg'), 'w') as f:
        f.write(template)
    configurator = Configurator(
        template='bobtemplates.cs:cs_plone_buildout',
        target_directory=target_dir,
        variables={'year': 1970, 'plone.version': '5.0-latest'},
    )
    base.set_global_vars(configurator)

    configurator = Configurator(
        template='bobtemplates.cs:cs_plone_buildout',
        target_directory=target_dir,
        variables={'year': 1970},
    )
    base.set_global_vars(configurator)
