import shutil
from pathlib import Path
import os
from .file_tree import generate_files_tree
from .log import log


def walk(src, dst, log_path):
    """
       Recursively traverses through implicit files tree of given directory replicating files that are 
       present in target directory. Preserves permisions. 
       This approach: to walk on each iteration for one layer of implicit files tree was choosed for
       simplicity and because it seems to be not hard to parallelise.
    
    """
    src = Path(src)
    dst = Path(dst)
    src_file_tree = generate_files_tree(src)
    dst_file_tree = generate_files_tree(dst)
    for k, v in src_file_tree.items():
        if v.name in dst_file_tree and v.stat().st_size == dst_file_tree[
                v.name].stat().st_size:
            src_stat = os.stat(v.path)
            dst_stat = os.stat(dst_file_tree[v.name])
            if src_stat.st_size == dst_stat.st_size:
                if src_stat.st_mode != dst_stat.st_mode:
                    os.chmod(dst_file_tree[v.name].path, src_stat.st_mode)
            if v.is_dir():
                walk(src / v.name, dst / v.name, log_path)
        else:
            if v.is_dir():
                path = dst / v.name
                path.mkdir(mode=v.stat().st_mode, parents=True)
                log(log_path, 'mkdir', str(path))
                walk(src / v.name, dst / v.name, log_path)
            else:
                shutil.copy2(v.path, dst)  #TODO
                log(log_path, 'cp', str(v.path))


def backwalk(src, dst, log_path):
    """Performs recursive deletiion of files that are not present in source directory. Note that 
       src is path to source dir to maintain consistency with the walk function. 
    """
    src = Path(src)
    dst = Path(dst)
    src_file_tree = generate_files_tree(src)
    dst_file_tree = generate_files_tree(dst)
    for k, v in dst_file_tree.items():
        if v.name not in src_file_tree:
            if v.is_dir():
                shutil.rmtree(v.path)  #TODO: errors???!!!
                log(log_path, 'rm', str(v.path))
            else:
                os.remove(v.path)
                log(log_path, 'rm', str(v.path))
        else:
            if v.is_dir():
                backwalk(src / v.name, dst / v.name, log_path)