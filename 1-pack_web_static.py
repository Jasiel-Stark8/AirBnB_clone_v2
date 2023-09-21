#!/usr/bin/python3
"""
Fabric script to generate a .tgz archive from the contents of web_static
"""

from fabric.api import local
from datetime import datetime

def do_pack():
    """Generate .tgz archive from the contents of the web_static folder."""
    # Create the versions directory if it doesn't exist
    local("mkdir -p versions")

    # Generate the .tgz archive
    time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(time_stamp)
    result = local("tar -czvf {} web_static".format(archive_path))

    # Return the archive path if successful, otherwise None
    if result.failed:
        local("Failed to create archive")
    return archive_path
