#!/usr/bin/python3
"""tgz archive of web_static folder"""

from datetime import datetime
from fabric.api import local


def do_pack():
    """Generate the .tgz archive from web_static"""

    dt = datetime.now()
    now = dt.strftime('%Y%m%d%H%M%S')

    local("mkdir -p versions")
    location = "versions/web_static_{}.tgz".format(now)
    result = local("tar -czvf {} web_static".format(location))

    if result.succeeded:
        return location
    else:
        return None
