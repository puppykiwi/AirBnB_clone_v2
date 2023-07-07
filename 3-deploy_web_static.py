#!/usr/bin/python3
"""a fabfile that generates a .tgz archive from the contents of the web_static folder"""

from fabric.api import *
from fabric.operations import *
from datetime import datetime
from os import path

env.hosts = ['54.173.175.228','52.73.248.17']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'

def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""
    date = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(date.year, date.month, date.day, date.hour, date.minute, date.second)

    if path.isdir("versions") is False:
        local("mkdir -p versions")

    if local("tar -cvzf {} web_static".format(file)).failed is False:
        return file
    else:
        return None

def do_deploy(archive_path):
    """distributes an archive to your web servers.
    Args:
        archive_path (string): path to archive
    Returns:
        Boolean: whether the archive is distributed or not
    """

    if path.isfile(archive_path) is False:
        return False

    file_name = path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)
    success = False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")
        # create the folder /data/web_static/releases/<archive filename without extension> on the web server
        run("mkdir -p {}".format(folder_path))
        # Uncompress the archive to the folder /data/web_static/releases/<archive filename without extension> on the web server
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
        # move the extracted folder to the desired location (..)
        run("mv {}web_static/* {}".format(folder_path, folder_path))
        # remove the old folder
        run("rm -rf {}web_static".format(folder_path))
        # Delete the archive from the web server
        run("rm /tmp/{}".format(file_name))
        # remove the symbolic link /data/web_static/current from the web server
        run("rm -rf /data/web_static/current")
        # Create a new the symbolic link /data/web_static/current on the web server, linked to the new version of your code
        run("ln -s {} /data/web_static/current".format(folder_path))

        success = True
        print("New version deployed!")
    except Exception as e:
        success = False
        print("Deployment failed: {}".format(e))

    return success

def deploy():
    """creates and distributes an archive to your web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

deploy()