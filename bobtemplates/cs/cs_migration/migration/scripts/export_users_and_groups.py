"""
    Run this file in your source Plone site.

    It will create a folder called "99" with two files, one for users and the other for groups.
    If for some reason you need to rename that folder, change the value of the folder_name variable below.

    Copy the folder to your transmogrifier export folder.

    Run this script as follows:
        $ bin/instance run export_users.py
"""

import os
import simplejson as json

# Set here the id of your Plone site
site = app.Plone

folder_name = "99"

os.mkdir(folder_name)
counter = 99000

uf = site.acl_users
users = uf.source_users.getUsers()

exported_users = {"_acl_users": dict()}

for user in users:
    user_data = {
        "email": user.getProperty("email"),
        "fullname": user.getProperty("fullname"),
        "roles": user.getRoles(),
    }
    exported_users["_acl_users"][user._id] = user_data

f = open(os.path.join("99", str(counter) + ".json"), "wb")
json.dump(exported_users, f, indent=4)
counter += 1
f.close()

groups = dict(uf.source_groups._groups)
exported_groups = {"_acl_groups": dict()}
for group in groups:
    # Loop over each group grabbing members
    members = uf.source_groups._group_principal_map[group].keys()
    roles = uf.getGroupByName(group)._roles
    group_info = {
        "title": groups[group]["title"],
        "description": groups[group]["description"],
        "members": members,
        "roles": roles,
    }
    exported_groups["_acl_groups"][group] = group_info

f = open(os.path.join(folder_name, str(counter) + ".json"), "wb")
json.dump(exported_groups, f, indent=4)
counter += 1
f.close()
