from utils import file_tree
import os
import shutil
import walk_tree_test


def create_test_dir():
    os.mkdir('./testdir')
    os.mkdir('./testdir/nesteddir1')
    os.mkdir('./testdir/nesteddir2')


def create_empty_test_dir():
    os.mkdir('./testdir')


def rm_test_dir():
    #os.chmod('/testdir', 16877)
    shutil.rmtree('./testdir')


def test_basic():
    try:
        rm_test_dir()
    except FileNotFoundError:
        pass
    create_test_dir()
    walk_tree_test.create_log_dir()
    t = file_tree.generate_files_tree('./testdir', './log/log')
    assert len(t) == 2
    rm_test_dir()
    walk_tree_test.rm_log_dir()


def test_empty():
    walk_tree_test.create_log_dir()
    create_empty_test_dir()
    t = file_tree.generate_files_tree('./testdir', './log/log')
    assert [] == [k for k, v in t.items()]
    rm_test_dir()
    walk_tree_test.rm_log_dir()
