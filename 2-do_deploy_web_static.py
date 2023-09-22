#!/usr/bin/python3
"""
This Fabric script deploys the web_Static archive to \
251279-web-01 ubuntu@18.204.5.218 & 251279-web-02 ubuntu@100.26.218.215
"""

from fabric.api import local
from datetime import datetime

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
    """Distributes an archive to web servers."""
    # Check if the archive exists
    if not exists(archive_path):
        return False

    try:
        # Extract the archive filename without extension
        archive_name = archive_path.split("/")[-1]
        without_extension = archive_name.split(".")[0]

        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Uncompress the archive to the folder on the web server
        run("mkdir -p /data/web_static/releases/{}/".format(without_extension))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/ \
            ".format(archive_name, without_extension))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(archive_name))

        # Delete the symbolic link /data/web_static/current from the web server
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link on the web server
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current \
            ".format(without_extension))

        return True
    except:
        return False
