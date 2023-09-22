#!/usr/bin/python3
"""
This Fabric script creates & distributes the web_Static archive to \
251279-web-01 ubuntu@18.204.5.218 & 251279-web-02 ubuntu@100.26.218.215 \
using the function deploy
"""

import os
from datetime import datetime
from fabric.api import *

# Set the host IP addresses for 251279-web-01 && 251279-web-02 & authenticate
env.hosts = ['ubuntu@18.204.5.218', 'ubuntu@100.26.218.215'] # Explicitly add ubuntu@<ip_Address>  --strick_Auth
env.user = "ubuntu"
env.key_filename = '/root/.ssh/id_rsa' # Authorization key

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
    return False

def deploy():
    """Creates and distributes an archive to web servers."""
    # Call the do_pack() function
    archive_path = do_pack()

    # Check if archive was created
    if not archive_path:
        return False

    # Call the do_deploy() function
    return do_deploy(archive_path)

def do_clean(number=0):
    """Deletes out-of-date archives of the static files.
    Args:
        number (Any): The number of archives to keep.
    """
    archives = os.listdir('versions/')
    archives.sort(reverse=True)
    start = int(number)
    if not start:
        start += 1
    if start < len(archives):
        archives = archives[start:]
    else:
        archives = []
    for archive in archives:
        os.unlink('versions/{}'.format(archive))
    cmd_parts = [
        "rm -rf $(",
        "find /data/web_static/releases/ -maxdepth 1 -type d -iregex",
        " '/data/web_static/releases/web_static_.*'",
        " | sort -r | tr '\\n' ' ' | cut -d ' ' -f{}-)".format(start + 1)
    ]
    run(''.join(cmd_parts))
