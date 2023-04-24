#!/usr/bin/python3
# A Fabscript that creates .tgz archive from web static.
import os.path
from fabric.api import local
from datetime import datetime

def do_pack():
    """Creates an archive of web static."""
    dt = datetime.utcnow()
    archive = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    ver_check = os.path.isdir("versions")
    arch_output = local("tar -cvzf {} web_static".format(archive)).failed
    if ver_check is False:
        if local("mkdir -p versions").failed:
            return None
    if arch_output:
        return None
    return
