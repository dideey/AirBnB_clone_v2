#!/usr/bin/python3
"""A fabric script that distributes archive
   to the web servers
"""
from fabric.api import *


def do_deploy(archive_path):
    """deploys web_static
    """
    if not archive_path:
        return False
    try:
        put("archive_path", "/tmp/")
        archive_filename = archive_path.split('/')[-1]
        archive_folder = '/data/web_static/releases/{}'.format(
            archive_filename[:-4])
        run('sudo mkdir -p {}.formart(archive_folder)')
        run('sudo tar -xzf /tmp/{}'.format(archive_filename, archive_folder))
        run('sudo rm /tmp/{}'.format(archive_filename))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/web_static/current'.format(archive_folder))
        return True
    except:
        return False
