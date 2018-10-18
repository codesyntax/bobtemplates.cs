# -*- coding: utf-8 -*-
from datetime import date

import logging


logger = logging.getLogger('bobtemplates.cs')


class SetupCfg(object):
    def __init__(self):
        self.version = None


def set_global_vars(configurator):
    configurator.variables['year'] = date.today().year
    version = configurator.variables.get('plone.version')
    _set_plone_version_variables(configurator, version)


def _set_plone_version_variables(configurator, version):
    version = configurator.variables.get('plone.version', version)
    if not version:
        return
    if 'plone.is_plone5' not in configurator.variables:
        # Find out if it is supposed to be Plone 5.
        if version.startswith('5'):
            configurator.variables['plone.is_plone5'] = True
        else:
            configurator.variables['plone.is_plone5'] = False
    if 'plone.minor_version' not in configurator.variables:
        # extract minor version (4.3)
        # (according to https://plone.org/support/version-support-policy)
        # this is used for the trove classifier in setup.py of the product
        configurator.variables['plone.minor_version'] = \
            '.'.join(version.split('.')[:2])
