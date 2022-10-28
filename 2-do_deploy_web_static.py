#!/usr/bin/python3
'''This fabric file is used to simplify deployment of web_static

    Functions:
        do_pack - creates an archive for of the webstatic in versions
                  folder
        do_deploy - distributes an archive to the web servers
'''
from fabric.api import *
from datetime import datetime
import os


env.hosts = [
    '3.215.16.116',
    '100.25.199.54'
]
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


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


def do_deploy(archive_path):
    '''Moves an archive to the web servers
    '''
    if not os.path.exists(archive_path):
        return False
    archive_name = archive_path.split('/')[-1]
    folder_name = archive_name[:-4]
    if put(local_path=archive_path, remote_path="/tmp/").failed:
        return False
    if run("mkdir -p /data/web_static/releases/{}".format(folder_name)).failed:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
            archive_name, folder_name)).failed:
        return False
    if run("rm /tmp/{}".format(archive_name)).failed:
        return False
    if run("mv /data/web_static/releases/{}/web_static/*\
 /data/web_static/releases/{}/".format(folder_name, folder_name)).failed:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".format(
            folder_name)).failed:
        return False
    if run("rm -rf /data/web_static/current").failed:
        return False
    if run(
            "ln -s /data/web_static/releases/{}\
 /data/web_static/current".format
            (folder_name)).failed:
        return False
    return True
