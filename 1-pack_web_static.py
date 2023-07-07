#!/usr/bin/python3
# a fabfile that generates a .tgz archive from the contents of the web_static

from fabric.api import local
from datetime import datetime
from os import path

def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""
    date = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(date.year, date.month, date.day, date.hour, date.minute, date.second)

    if path.isdir("versions") is False:
        local("mkdir -p versions")

    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    else:
        return file

do_pack()