"""Module provides operation to move files.

:Author: alevyts
"""
import shutil


def move(filename, repo, ssh_url):
    git = repo.git
    git.remote('add', 'origin', ssh_url)
    git.config('core.sparsecheckout', 'true')
    with open('tmp/.git/info/sparse-checkout', 'w') as f:
        f.write(filename)
    git.pull('origin', 'develop')
    return git


def new_move(filename, repo):
    git = repo.git
    git.config('core.sparsecheckout', 'true')
    with open('tmp/.git/info/sparse-checkout', 'w') as f:
        f.write(filename)
    git.read_tree('-mu', 'HEAD')


def clear(path):
    """Remove temporary data file"""
    shutil.rmtree(path)
