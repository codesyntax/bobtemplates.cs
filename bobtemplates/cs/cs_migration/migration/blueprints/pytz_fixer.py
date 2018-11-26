# -*- coding: utf-8 -*-
"""
Original: https://gist.github.com/gyst/c3739160a18cf52c93e0132da511b2ee

see https://stackoverflow.com/questions/4008960/pytz-and-etc-gmt-5
for GMT+ and GMT- bug
"""
from collective.transmogrifier.interfaces import ISection
from collective.transmogrifier.interfaces import ISectionBlueprint
from collective.transmogrifier.utils import Condition
from collective.transmogrifier.utils import Matcher
from zope.interface import classProvides
from zope.interface import implements

import logging


logger = logging.getLogger(__name__)


class TimezoneFixerSection(object):
    """
    Fixes UnknownTimeZoneError: (UnknownTimeZoneError('GMT+1',),
    by replacing the (unknown) GMT+x timezone with Etc/GMT+x
    """

    classProvides(ISectionBlueprint)
    implements(ISection)

    def __init__(self, transmogrifier, name, options, previous):
        keys = options.get('keys') or 'regexp:(.*[Dd]ate)$'
        self.keys = Matcher(*keys.splitlines())
        self.condition = Condition(
            options.get('condition', 'python:True'),
            transmogrifier,
            name,
            options,
        )
        self.previous = previous

    def __iter__(self):
        for item in self.previous:
            if self.condition(item):
                for key in item.keys():
                    match = self.keys(key)[1]
                    if match:
                        oldvalue = item[key]
                        if 'GMT+' in item[key]:
                            item[key] = item[key].replace(
                                ' GMT+', ' Etc/GMT-'
                            )  # noqa
                        elif 'GMT-' in item[key]:
                            item[key] = item[key].replace(
                                ' GMT-', ' Etc/GMT+'
                            )  # noqa
                        elif 'GMT' in item[key]:
                            item[key] = item[key].replace(' GMT', ' Etc/GMT')

                        newvalue = item[key]
                        if oldvalue != newvalue:
                            logger.info(
                                'pytz_fixer: field: {}, oldvalue {} newvalue {}'.format(  # noqa
                                    key, oldvalue, newvalue
                                )
                            )
            yield item
