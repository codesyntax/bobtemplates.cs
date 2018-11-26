# -*- coding: utf-8 -*-
from AccessControl.SecurityManagement import newSecurityManager
from AccessControl.SecurityManager import setSecurityPolicy
from collective.transmogrifier.transmogrifier import configuration_registry
from collective.transmogrifier.transmogrifier import Transmogrifier
from Products.CMFCore.tests.base.security import OmnipotentUser
from Products.CMFCore.tests.base.security import PermissiveSecurityPolicy
from Testing.makerequest import makerequest
from zope.site.hooks import setSite

import logging
import sys
import transaction


# Force application logging level to INFO and
# log output to stdout for all loggers
root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s')
handler.setFormatter(formatter)
root_logger.addHandler(handler)


def spoofRequest(app):
    """
    Make REQUEST variable to be available on the Zope application server.

    This allows acquisition to work properly
    """
    _policy = PermissiveSecurityPolicy()
    _oldpolicy = setSecurityPolicy(_policy)  # NOQA F841
    newSecurityManager(None, OmnipotentUser().__of__(app.acl_users))
    return makerequest(app)


def run_migration(self, *args):
    call = args[0]
    if len(call) > 2:
        pipeline_id = call[2]
        for plonesite in self.objectValues('Plone Site'):
            setSite(plonesite)
            plonesite = spoofRequest(plonesite)
            if pipeline_id in configuration_registry.listConfigurationIds():
                transmogrifier = Transmogrifier(plonesite)
                overrides = {}
                if len(call) >= 4:
                    json_path = call[3]
                    overrides['jsonsource'] = {'path': json_path}

                transmogrifier(pipeline_id, **overrides)
                transaction.commit()
                print('All set!')
            else:
                print('This migration id is invalid.')

    else:
        print('You need to tell me the migration id to run')
