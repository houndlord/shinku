import os 


def generate_files_tree(path):
    files_tree = {}
    with os.scandir(path) as it: #may throw exception
        for entry in it:
            files_tree[entry.name] = entry
    return files_tree

