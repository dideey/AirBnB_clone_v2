#!/usr/bin/python3

"""A Fabric script that generates a .tgz archive
   from the contents of the web_static folder
"""
from fabric.api import *
from datetime import datetime


def do_pack():

    """"Creates the .tgz files"""

    local("sudo mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file = "versions/web_static_{}.tgz".format(date)
    archive = local("sudo tar -cvzf {} web_static".format(file))
    if archive.succeeded:
        return file
    else:
        return None
