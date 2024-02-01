#!/usr/bin/python3
"""A fabric script that distributes archive
   to the web servers
"""
from fabric.api import *
from os.path import exists
env.hosts = ['	54.237.80.147', '100.24.235.237']


def do_deploy(archive_path):
    """ distributes an archive to your web servers
    """
    if exists(archive_path) is False:
        return False
    file = archive_path.split('/')[-1]
    extract_tgz = '/data/web_static/releases/'\
        + "{}".format(file.split('.')[0])
    tmp = "/tmp/" + file

    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}/".format(extract_tgz))
        run("sudo tar -xzf {} -C {}/".format(tmp, extract_tgz))
        run("sudo rm {}".format(tmp))
        run("sudo mv {}/web_static/* {}/".format(extract_tgz, extract_tgz))
        run("sudo rm -rf {}/web_static".format(extract_tgz))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {}/ /data/web_static/current".format(extract_tgz))
        return True
    except Exception:
        return False
