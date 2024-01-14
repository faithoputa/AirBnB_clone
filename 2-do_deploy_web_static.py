#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""
from fabric.api import put, run, env
from os.path import exists, splitext
env.hosts = ['142.44.167.228', '144.217.246.195']


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
        run('mv {}/* {}'.format(path, path))
        run('rm -rf {}'.format(path + "/web_static"))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(path))
        return True
    except Exception as e:
        print(f"Error during deployment: {e}")
        return False

