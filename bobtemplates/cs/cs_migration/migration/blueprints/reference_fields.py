# -*- coding: utf-8 -*-
from collective.transmogrifier.interfaces import ISection
from collective.transmogrifier.interfaces import ISectionBlueprint
from z3c.relationfield import RelationValue
from zope.component import getUtility
from zope.event import notify
from zope.interface import classProvides
from zope.interface import implements
from zope.intid.interfaces import IIntIds
from zope.lifecycleevent import ObjectModifiedEvent


class References(object):
    classProvides(ISectionBlueprint)
    implements(ISection)

    def __init__(self, transmogrifier, name, options, previous):
        self.previous = previous
        self.context = transmogrifier.context
        self.deferred_references = {}
        self.reference_fields = options.get('keys') or 'regexp:(.*[Dd]ate)$'

    def __iter__(self):
        for item in self.previous:
            for fieldname in self.reference_fields:
                if item.get(fieldname, ''):
                    references = self.deferred_references.get(fieldname, [])
                    references.append((item['_path'], item[fieldname]))
                    self.deferred_references[fieldname] = references

            yield item

        intids = getUtility(IIntIds)
        for fieldname, references in self.deferred_references.items():
            for path, uid in references:
                items = []
                try:
                    referencer_object = self.context.restrictedTraverse(
                        str(path)
                    )
                except KeyError:
                    continue

                referenced_brains = self.context.portal_catalog(UID=uid)
                if referenced_brains:
                    referenced_brain = referenced_brains[0].getObject()
                    try:
                        to_id = intids.getId(referenced_brain)
                    except KeyError:
                        to_id = intids.register(referenced_brain)
                    items.append(RelationValue(to_id))

                    setattr(referencer_object, fieldname, items[0])
                    notify(ObjectModifiedEvent(referencer_object))
