import os
from .log import log
import sys


def generate_files_tree(path):
    """
       Generates dictionary of all files in given directory.
    """
    files_tree = {}
    try:
        with os.scandir(path) as it:  #may throw exception
            for entry in it:
                files_tree[entry.name] = entry
        return files_tree
    except PermissionError:
        log('perm', path)
        print('xyj')
        sys.exit()
