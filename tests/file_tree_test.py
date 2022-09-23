from utils import file_tree
import os 
import shutil


def create_test_dir():
    os.mkdir('./testdir')
    os.mkdir('./testdir/nesteddir1')
    os.mkdir('./testdir/nesteddir2')

def create_empty_test_dir():
    os.mkdir('./testdir')

def rm_test_dir():
    shutil.rmtree('./testdir')

def test_basic():
    try:
        rm_test_dir()
    except FileNotFoundError:
        pass
    create_test_dir()
    t = file_tree.generate_files_tree('./testdir')
    assert ['nesteddir1', 'nesteddir2'] == [k for k, v in t.items()]
    rm_test_dir()

def test_empty():
    create_empty_test_dir()
    t = file_tree.generate_files_tree('./testdir')
    assert [] == [k for k, v in t.items()]
    rm_test_dir()
