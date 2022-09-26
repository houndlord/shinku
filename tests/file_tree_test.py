from utils import file_tree
import os
import shutil
import walk_tree_test


def create_empty_test_dir():
    try:
        os.mkdir('./testdir')
    except FileExistsError:
        rm_test_dir()


def rm_test_dir():
    os.chmod('./testdir', 16877)
    shutil.rmtree('./testdir')


def test_basic():
    walk_tree_test.create_test_dir()
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
