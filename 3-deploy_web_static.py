#!/usr/bin/python3
"""
Fabric script based on the file 2-do_deploy_web_static.py that creates
and distributes an archive to the web servers
"""
from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir, splitext
env.hosts = ['142.44.167.228', '144.217.246.195']


def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        versions_dir = "versions"
        archive_name = f"web_static_{date}.tgz"
        archive_path = f"{versions_dir}/{archive_name}"
        if not isdir(versions_dir):
            local("mkdir -p {}".format(versions_dir))
        local("tar -czf {} web_static".format(archive_path))
        return archive_path
    except Exception as e:
        print(f"Error during packaging: {e}")
        return None


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = splitext(archive_path.split("/")[-1])[0]
        path = "/data/web_static/releases/{}".format(file_name)
        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(path))
        run('tar -xzf /tmp/{} -C {}'.format(archive_path.split("/")[-1], path))
        run('rm /tmp/{}'.format(archive_path.split("/")[-1]))
        run('mv {}web_static/* {}'.format(path, path))
        run('rm -rf {}web_static'.format(path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(path))
        return True
    except Exception as e:
        print(f"Error during deployment: {e}")
        return False


def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

