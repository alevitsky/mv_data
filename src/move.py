"""Module provides operation to move files.

:Author: alevyts
"""


def move(filename, repo, ssh_url):
    git = repo.git
    git.remote('add', 'origin', ssh_url)
    git.config('core.sparsecheckout', 'true')
    with open('.git/info/sparse-checkout', 'w') as f:
        f.write(filename)
    git.pull('origin', 'develop')


def new_move():
    pass


def clear():
    pass
