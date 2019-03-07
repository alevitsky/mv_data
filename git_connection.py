"""Module provides connection to github.

:Author: alevyts.
"""
import os
from git import Repo


def login_to_github(ssh_url=None, https_url=None, ssh_key_path=None,
                    username=None, password=None):
    """Make connection to GitHub with ssh or https

    :Parameters:
    - `ssh_url`: url to use an SSH key to add a new remote.
    - `http_url`: url to using the web URL to add a new remote.
    - `ssh_key_path`: path to ssh_key for setting ssh connection.
    - `username`: username for github account.
    - `password`: password for github account.
    """
    if ssh_url:
        repo_dir = os.path.join(os.getcwd(), 'tmp')
        repo = Repo.init(repo_dir,
                         env={"GIT_SSH_COMMAND": 'ssh -i {path}'
                              .format(path=ssh_key_path)})
        return repo
