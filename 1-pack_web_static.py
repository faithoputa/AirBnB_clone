#!/usr/bin/python3

"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""

from datetime import datetime
from fabric.api import local, env
from distutils.dir_util import copy_tree
from pathlib import Path

env.hosts = []

def do_pack():
    """generates a tgz archive from the web_static folder"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        versions_dir = Path("versions")
        web_static_dir = Path("web_static")

        if not versions_dir.exists():
            versions_dir.mkdir()

        archive_name = f"web_static_{date}.tgz"
        archive_path = versions_dir / archive_name

        if web_static_dir.exists():
            copy_tree("web_static", versions_dir / "web_static_copy")
            local(f"tar -czvf {archive_path} -C {versions_dir} web_static_copy")
            return archive_name
        else:
            print("web_static directory does not exist")
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

