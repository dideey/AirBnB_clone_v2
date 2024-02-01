#!/usr/bin/python3
"""A fabric script that distributes archive
   to the web servers
"""
from fabric.api import *
env.hosts = ['	54.237.80.147', '100.24.235.237']


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
        run('sudo tar -xzf /tmp/{} -C {}'.format(archive_filename, archive_folder))
        run('sudo rm /tmp/{}'.format(archive_filename))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(archive_folder))
        run('rm -rf {}/web_static'.format(archive_folder))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/web_static/current'.format(archive_folder))
        return True
    except:
        return False
