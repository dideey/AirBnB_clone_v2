#!/usr/bin/python3
"""Fabric script that creates and distributes
   an archive to my web servers
"""
from fabric.api import *
from os.path import exists
from datetime import datetime
env.hosts = ['	54.237.80.147', '100.24.235.237']


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


def do_deploy(archive_path):
    """deploys web_static
    """
    if exists(archive_path) is False:
        return False
        archive_filename = archive_path.split('/')[-1]
        archive_folder = '/data/web_static/releases/{}'.format(
            archive_filename.split('.')[0])
    try:
        put(archive_path, "/tmp/")
        run('sudo mkdir -p {}./'.format(archive_folder))
        run('sudo tar -xzf /tmp/{} -C {}/'.format(
            archive_filename, archive_folder))
        run('sudo rm /tmp/{}'.format(archive_filename))
        run("sudo mv {}/web_static/* {}/".format(
            archive_folder, archive_folder))
        run("sudo rm -rf {}/web_static".format(archive_folder))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/web_static/current'.format(archive_folder))
        return True
    except Exception:
        return False


def deploy():
    """deploys fully
    """
    new_archive = do_pack
    if exists(new_archive) is False:
        return False
    return do_deploy(new_archive)
