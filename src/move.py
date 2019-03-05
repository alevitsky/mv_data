"""Module provides operation to move files.

:Author: alevyts
"""


def move(filename, repo):
    with open('.git/info/sparse-checkout', 'w') as f:
        f.write(filename)
    git = repo.git
    git.config('core.sparsecheckout', 'true')
    git.pull('origin', 'develop')
