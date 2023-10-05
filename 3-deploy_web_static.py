#!/usr/bin/python3
""" Fabric script (based on the file 2-do_deploy_web_static.py) that creates
and distributes an archive to your web servers, using the function deploy: """


from fabric.api import *
from datetime import datetime
from os.path import exists



env.hosts = ['52.3.220.51', '54.89.135.205']



def do_pack():
    """generates a .tgz archive from the contents of the web_static folder
    """
