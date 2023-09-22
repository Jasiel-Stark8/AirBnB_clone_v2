#!/usr/bin/python3
"""
This Fabric script deploys the web_Static archive to \
251279-web-01 ubuntu@18.204.5.218 & 251279-web-02 ubuntu@100.26.218.215
"""

import os
from datetime import datetime
from fabric.api import local, put, run, env

# Declare web servers
env.hosts = ['18.204.5.218', '100.26.218.215']
env.user = "ubuntu"

def do_pack():
    """Generates .tgz archive from the contents of the web_static folder."""
    # Current date and time object
    time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")

    # Define path where archive will be saved
    archive_path = "versions/web_static_{}.tgz".format(time_stamp)

    # Create the versions directory if it doesn't exist
    local("mkdir -p versions")

    # Use tar command to create a compresses archive
    result = local("tar -cvzf {} web_static".format(archive_path))

    # Return the archive path if successful, else None (Check archive status)
    if result.return_code != 0:
        return None
    else:
        return archive_path

def do_deploy(archive_path):
    '''use os module to check for valid file path'''
    try:
        if os.path.exists(archive_path):
            archive = archive_path.split('/')[1]
            a_path = "/tmp/{}".format(archive)
            folder = archive.split('.')[0]
            f_path = "/data/web_static/releases/{}/".format(folder)

            put(archive_path, a_path)
            run("mkdir -p {}".format(f_path))
            run("tar -xzf {} -C {}".format(a_path, f_path))
            run("rm {}".format(a_path))
            run("mv -f {}web_static/* {}".format(f_path, f_path))
            run("rm -rf {}web_static".format(f_path))
            run("rm -rf /data/web_static/current")
            run("ln -s {} /data/web_static/current".format(f_path))
            return True
    except:
        return False
