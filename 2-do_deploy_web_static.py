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
        basename = os.path.basename(archive_path)
        if basename[-4:] == ".tgz":
            name = basename[:-4]
        res = put(archive_path, "/tmp")
        results.append(res.succeeded)

        basename = os.path.basename(archive_path)
        if basename[-4:] == ".tgz":
            name = basename[:-4]
        newdir = "/data/web_static/releases/" + name
        run("sudo mkdir -p " + newdir)
        run("sudo tar -xzf /tmp/" + basename + " -C " + newdir)

        run("sudo rm /tmp/" + basename)

        run("sudo rsync -a /data/web_static/releases/{}/web_static/ {}/"
            .format(name, newdir))
        run("sudo rm -rf " + newdir + "/web_static")

        current_path = "/data/web_static/current"
        run("sudo rm -rf {}".format(current_path))
        run("sudo ln -s {} {}".format(newdir, current_path))

        return True

    return False
