#!/usr/bin/python3
""" Deployment"""

from fabric.api import *
import os

env.hosts = ["34.232.53.87", "100.25.10.249"]
env.user = "ubuntu"


def do_deploy(archive_path):
    """ Deploys archive to servers"""
    if not os.path.exists(archive_path):
        return False

    results = []

    res = put(archive_path, "/tmp")
    results.append(res.succeeded)

    basename = os.path.basename(archive_path)
    if basename[-4:] == ".tgz":
        name = basename[:-4]
    newdir = "/data/web_static/releases/" + name
    run("sudo mkdir -p " + newdir)
    run("sudo tar -xzf /tmp/" + basename + " -C " + newdir)

    run("sudo rm /tmp/" + basename)

    run("sudo rsync -a /data/web_static/releases/{}/web_static/ {}/".format(name, newdir))
    run("sudo rm -rf " + newdir + "/web_static")

    current_path = "/data/web_static/current"
    run("sudo rm -rf {}".format(current_path))
    run("sudo ln -s {} {}".format(newdir, current_path))

    return True
