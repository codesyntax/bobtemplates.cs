# -*- coding: utf-8 -*-
from bobtemplates.plone.base import base_prepare_renderer
from bobtemplates.plone.base import git_commit
from bobtemplates.plone.base import is_string_in_file
from bobtemplates.plone.base import set_global_vars as base_set_global_vars
from bobtemplates.plone.base import update_file


def _update_setup_py(configurator):
    file_name = u"setup.py"
    file_path = configurator.variables["package.root_folder"] + "/" + file_name
    match_str = "-*- Extra requirements: -*-"
    insert_strings = [
        "collective.transmogrifier",
        "plone.app.transmogrifier",
        "transmogrify.dexterity",
        "ftw.blueprints",
        "collective.jsonmigrator",
    ]
    for insert_str in insert_strings:
        insert_str = "        '{0}',\n".format(insert_str)
        if is_string_in_file(configurator, file_path, insert_str):
            continue
        update_file(configurator, file_path, match_str, insert_str)

    match_str = "target = plone"
    insert_strings = [
        "run_migration = {0}.migration.scripts:run_migration".format(
            configurator.variables["package.dottedname"]
        ),
        "list_migrations = {0}.migration.scripts:list_migrations".format(
            configurator.variables["package.dottedname"]
        ),
        "[zopectl.command]",
    ]
    for insert_str in insert_strings:
        insert_str = "    {0}\n".format(insert_str)
        if is_string_in_file(configurator, file_path, insert_str):
            continue
        update_file(configurator, file_path, match_str, insert_str)


def _update_configure_zcml(configurator):
    file_name = u"configure.zcml"
    file_path = configurator.variables["package_folder"] + "/" + file_name

    match_str = "-*- extra stuff goes here -*-"
    insert_str = """
  <include package=".migration" />
"""
    update_file(configurator, file_path, match_str, insert_str)


def prepare_renderer(configurator):
    configurator = base_prepare_renderer(configurator)
    configurator.target_directory = configurator.variables["package_folder"]


def post_renderer(configurator):
    _update_setup_py(configurator)
    _update_configure_zcml(configurator)
    git_commit(configurator, "Added migration")


def set_global_vars(configurator):
    base_set_global_vars(configurator)
