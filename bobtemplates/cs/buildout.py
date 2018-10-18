# -*- coding: utf-8 -*-


def prepare_renderer(configurator):
    configurator.variables['template_id'] = 'cs_plone_buildout'
    zope_port_number = int(configurator.variables['buildout_zope_port_number'])
    configurator.variables['zope_instance2_port_number'] = zope_port_number + 1
    configurator.variables['zope_instance3_port_number'] = zope_port_number + 2
    configurator.variables['zope_instance4_port_number'] = zope_port_number + 3
    configurator.variables['zope_instance5_port_number'] = zope_port_number + 4
    configurator.variables['zeo_port_number'] = zope_port_number + 10
    configurator.variables['haproxy_port_number'] = zope_port_number + 20
    configurator.variables['varnish_port_number'] = zope_port_number + 30


def post_renderer(configurator):
    """"""
    pass
