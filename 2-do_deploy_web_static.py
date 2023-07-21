#!/usr/bin/python3
""" Deployment"""

from fabric.api import *
from datetime import datetime
import os

env.hosts = ["34.232.53.87", "100.25.10.249"]
env.user = "ubuntu"


def do_pack():
    """Generates a .tgz archive from the content"""

    d = datetime.now()
    now = d.strftime('%Y%m%d%H%M%S')

    local("mkdir -p versions")
    local("tar -czvf versions/web_static_{}.tgz web_static".format(now))


def do_deploy(archive_path):
    """ Deploys archive to servers"""
    results = []

    # Local deployment
    if os.path.exists(archive_path):
        archive = archive_path.split('/')[1]
        a_path = "/tmp/{}".format(archive)
        folder = archive.split('.')[0]
        f_path = "/data/web_static/releases/{}/".format(folder)

        put(archive_path, a_path)
        run("sudo mkdir -p {}".format(f_path))
        run("sudo tar -xzf {} -C {}".format(a_path, f_path))
        run("sudo rm {}".format(a_path))
        run("sudo mv -fi {}web_static/* {}".format(f_path, f_path))
        run("sudo rm -rf {}web_static".format(f_path))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(f_path))
        return True

    return False
