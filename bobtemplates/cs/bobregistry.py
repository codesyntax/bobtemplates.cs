# -*- coding: utf-8 -*-


class RegEntry(object):
    def __init__(self):
        self.template = ''
        self.plonecli_alias = ''
        self.depend_on = None
        self.deprecated = False
        self.info = ''


def cs_plone_buildout():
    reg = RegEntry()
    reg.template = 'bobtemplates.cs:cs_plone_buildout'
    reg.plonecli_alias = 'cs_plone_buildout'
    return reg
