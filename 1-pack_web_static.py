#!/usr/bin/python3
""" Creates an archive from the content of web_static folder """
from fabric.api import *
from datetime import datetime
from fabric.decorators import runs_once


@runs_once
def do_pack():
    """ Creates archive of the web_static folder in
    versions/web_static_<year><month><day><hour><minute><second>.tgz"""
    created_at = datetime.now()
    archive_path =
    f"versions/web_static_{created_at.strftime('%Y%m%d%H%M%S')}.tgz"
    local("mkdir -p versions")
    print(f"Packing web_static to {archive_path}")
    result = local(f"tar -cvzf {archive_path} web_static")
    if result.succeeded:
        return archive_path
    return None
