#!/usr/bin/python3
"""  Fabric script (based on the file 1-pack_web_static.py) that distributes an archive to your web servers, using the function do_deploy """


from fabric.api import *
from datetime import datetime
from os.path import exists


env.hosts = ['52.3.220.51', '54.89.135.205']


def do_deploy(archive_path):
    """ ditstributes and archive to my web servers """
    if exists(archive_path) is False:
        return False
