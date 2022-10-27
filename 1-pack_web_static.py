#!/usr/bin/python3
""" Creates an archive from the content of web_static folder """
from fabric.api import local
from datetime import datetime


def do_pack():
    """ Creates archive of the web_static folder in
    versions/web_static_<year><month><day><hour><minute><second>.tgz"""
    created_at = datetime.now()
    archive_name = f"web_static_{created_at.strftime('%Y%m%d%H%M%S')}.tgz"
    local("mkdir -p versions")
    result = local(f"tar -cvzf versions/{archive_name} web_static/")
    if result.succeeded:
        return f"versions/{archive_name}"
    else:
        return None
