# -*- coding: utf-8 -*-
"""
https://training.plone.org/5/transmogrifier/users-migration.html

Export first all users and groups using the scripts in the scripts folder:



"""
from collective.transmogrifier.interfaces import ISection
from collective.transmogrifier.interfaces import ISectionBlueprint
from collective.transmogrifier.utils import defaultKeys
from collective.transmogrifier.utils import Matcher
from plone import api
from zope.interface import implementer
from zope.interface import provider

import base64
import logging
import os


logger = logging.getLogger(__name__)


@provider(ISectionBlueprint)
@implementer(ISection)
class ImportUsers(object):
    """Import users that had been exported
    with the custom export script
    """

    def __init__(self, transmogrifier, name, options, previous):
        self.previous = previous

    def __iter__(self):
        for item in self.previous:
            if "_acl_users" not in item:
                yield item
                continue

            for person in item["_acl_users"]:
                user = api.user.get(username=person)
                data = item["_acl_users"][person]
                roles = data["roles"]
                # remove these roles, they cannot be granted
                if "Authenticated" in data["roles"]:
                    roles.remove("Authenticated")
                if "Anonymous" in data["roles"]:
                    roles.remove("Anonymous")
                if not data["email"]:
                    data["email"] = "user@site.com"

                if user:
                    api.user.grant_roles(username=person, roles=roles)
                    user.setMemberProperties(
                        {
                            "email": data.get("email", ""),
                            "fullname": data.get("fullname", ""),
                        }
                    )
                else:
                    try:
                        user = api.user.create(
                            username=person,
                            email=data.get("email", ""),
                            properties={"fullname": data.get("fullname", "")},
                        )
                        api.user.grant_roles(username=person, roles=roles)
                    except ValueError as e:
                        logger.warn(
                            "Import User '{0}' threw an error: {1}".format(person, e)
                        )
            yield item


@provider(ISectionBlueprint)
@implementer(ISection)
class Groups(object):
    """Import groups that had been exported
    with the custom export script
    """

    def __init__(self, transmogrifier, name, options, previous):
        self.transmogrifier = transmogrifier
        self.name = name
        self.options = options
        self.previous = previous
        self.context = transmogrifier.context

        if "acl_groups-key" in options:
            groupskeys = options["acl_groups-key"].splitlines()
        else:
            groupskeys = defaultKeys(options["blueprint"], name, "acl_groups")
        self.groupskey = Matcher(*groupskeys)

    def __iter__(self):
        for item in self.previous:
            groupskey = self.groupskey(*item.keys())[0]

            if not groupskey:
                yield item
                continue

            group_tool = api.portal.get_tool(name="portal_groups")
            if "_acl_groups" not in item:
                yield item
                continue
            for group in item["_acl_groups"]:
                acl_group = api.group.get(groupname=group)
                props = item["_acl_groups"][group]
                if not acl_group:
                    acl_group = api.group.create(
                        groupname=group,
                        title=props["title"],
                        description=props["description"],
                        roles=props["roles"],
                    )
                else:
                    group_tool.editGroup(
                        group,
                        roles=props["roles"],
                        title=props["title"],
                        description=props["description"],
                    )
                for member in props["members"]:
                    acl_group.addMember(member)

            yield item
