"""Main controller.

:Author: alevyts
"""
import argparse

from git_connection import login_to_github
from src.move import move, move_to_dest, new_move, clear


def get_args():
    """Creation of argument parser and return parse arguments"""
    parser = argparse.ArgumentParser()
    operation_group = parser.add_mutually_exclusive_group(required=True)
    parser.add_argument(
        "-u", "--user", help="User name for GitHub", action="store",
        dest="user")
    parser.add_argument(
        "-p", "--password", help="User password for GitHub",
        action="store", dest="passwd")
    parser.add_argument(
        "-s", "--ssh", help="url to use an SSH key to add a new remote",
        action="store", dest="ssh")
    parser.add_argument(
        "-H", "--https", help="url to using the web URL to add a new remote",
        action="store", dest="https")
    parser.add_argument(
        "-k", "--key", help="path to ssh_key for setting ssh connection",
        action="store", dest="key")
    parser.add_argument(
        "-f", "--file", nargs='+', help="path to ssh_key for setting ssh connection",
        action="store", dest="file")
    parser.add_argument(
        "-i", "--input", help="path to ssh_key for setting ssh connection",
        action="store", dest="input")
    parser.add_argument(
        "-d", "--dest", help="path to ssh_key for setting ssh connection",
        action="store", dest="dest")
    parser.add_argument(
        "-P", "--path", help="path to ssh_key for setting ssh connection",
        action="store", dest="path")
    operation_group.add_argument(
        "-m", "--move", action="store_true", dest="move",
        help="Move data from path to destination")
    operation_group.add_argument(
        "-n", "--new", action="store_true",
        dest="new_move", help="New move data from path to destination")
    operation_group.add_argument(
        "-t", "--target", action="store_true",
        dest="target", help="Target destination")
    operation_group.add_argument(
        "-c", "--clear", action="store_true",
        dest="clear", help="Clear move")

    args = parser.parse_args()

    return args


def main():
    """Handles parse arguments and run the script."""

    args = get_args()

    ssh_url = args.ssh
    https_url = args.https
    ssh_key_path = args.key
    username = args.user
    password = args.passwd
    input_path = args.input
    dest_path = args.dest
    filenames = args.file
    path = args.path

    repo = login_to_github(ssh_url, https_url, ssh_key_path, username,
                           password)

    if args.move:
        move(filenames, repo, ssh_url)
    elif args.new_move:
        new_move(filenames, repo)
    elif args.target:
        move_to_dest(input_path, dest_path)
    elif args.clear:
        clear(path)


if __name__ == '__main__':
    main()
