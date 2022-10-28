#!/usr/bin/python3
""" This fabric file is used to simplify deployment of web_static

    Functions:
        do_pack - creates an archive for of the webstatic in versions
                  folder
"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """ Creates archive of the web_static folder in
        Format:
            versions/web_static_<year><month><day><hour><minute><second>.tgz
    """
    local("mkdir -p versions")
    archive_path = f"\
versions/web_static_{datetime.now().strftime('%Y%m%d%H%M%S')}.tgz"
    result = local(f"tar -cvzf {archive_path} web_static")
    if result.succeeded:
        return archive_path
    return None
