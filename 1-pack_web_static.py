#!/usr/bin/python3
'''This fabric file is used to simplify deployment of web_static

    Functions:
        do_pack - creates an archive for of the webstatic in versions
                  folder
'''
from fabric.api import *
from datetime import datetime


def do_pack():
    ''' Creates archive of the web_static folder in
        Format:
            versions/web_static_<year><month><day><hour><minute><second>.tgz
    '''
    local("mkdir -p versions")
    archive_path = "versions/web_static_{}.tgz".format(
        datetime.now().strftime('%Y%m%d%H%M%S'))
    result = local("tar -cvzf {} web_static".format(archive_path))

    if result.succeeded:
        return archive_path
    return None
