"""Module provides operation to move files.

:Author: alevyts
"""
import shutil


def move(filenames, repo, ssh_url):
    git = repo.git
    git.remote('add', 'origin', ssh_url)
    git.config('core.sparsecheckout', 'true')
    for filename in filenames:
        with open('tmp/.git/info/sparse-checkout', 'a') as f:
            f.writelines(filename + '\n')
    git.pull('origin', 'develop')
    return git


def new_move(filenames, repo):
    git = repo.git
    git.config('core.sparsecheckout', 'true')
    for filename in filenames:
        with open('tmp/.git/info/sparse-checkout', 'a') as f:
            f.writelines(filename + '\n')
    git.read_tree('-mu', 'HEAD')


def move_to_dest(input_path, dest_path):
    """Move to destination"""
    shutil.move(input_path, dest_path)


def clear(path):
    """Remove temporary data file"""
    shutil.rmtree(path)
