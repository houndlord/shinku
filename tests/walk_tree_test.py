import random
import string
from utils import walk
import shutil
import os

def gen_random_string():
    return ''.join(random.choice(string.ascii_letters) for i in range(random.randrange(0, 1000)))

def gen_random_string_len(length):
    return ''.join(random.choice(string.ascii_letters) for i in range(length))

def create_test_dir():
    os.mkdir('./testdir')
    os.mkdir('./testdir/nesteddir1')
    os.mkdir('./testdir/nesteddir2')

def rm_test_dir():
    shutil.rmtree('./testdir')

def rm_dst_dir():
    shutil.rmtree('./dst')

def create_dir_replicate_to():
    os.mkdir('./dst')

def create_test_file(path):
    with open(path, 'w') as f:
        f.write(gen_random_string())

def create_test_file_len(path, length):
    with open(path, 'w') as f:
        f.write(gen_random_string_len(length))

def create_log_dir():
    try:
        rm_log_dir()
    except FileNotFoundError:
        pass
    os.mkdir('./log')

def rm_log_dir():
    shutil.rmtree('./log')

def setup_dirs():
    try:
        rm_test_dir()
    except FileNotFoundError:
        pass
    try:
        rm_dst_dir()
    except FileNotFoundError:
        pass
    create_test_dir()
    create_dir_replicate_to()
    create_test_file('./testdir/f')
    create_log_dir()

def test_walk_basic():
    setup_dirs()
    walk.walk('./testdir', './dst', './log/log')
    f1 = open('./testdir/f')
    f2 = open('./dst/f')
    assert f1.read() == f2.read()
    f1.close()
    f2.close()
    rm_log_dir()

def test_walk_nested():
    setup_dirs()
    create_test_file('./testdir/nesteddir1/f')
    walk.walk('./testdir', './dst', './log/log')
    f1 = open('./testdir/nesteddir1/f')
    f2 = open('./dst/nesteddir1/f')
    assert f1.read() == f2.read()
    f1.close()
    f2.close()
    rm_log_dir()

def test_walk_file_change_basic():
    setup_dirs()
    walk.walk('./testdir', './dst', './log/log')
    f1 = open('./testdir/f', 'a')
    f1.write(gen_random_string_len(512))
    f1.close()
    walk.walk('./testdir', './dst', './log/log')
    f1 = open('./testdir/f')
    f2 = open('./dst/f')
    assert f1.read() == f2.read()
    f1.close()
    f2.close()
    rm_log_dir()

def test_walk_file_change_nested():
    setup_dirs()
    create_test_file('./testdir/nesteddir1/f')
    walk.walk('./testdir', './dst', './log/log')
    f1 = open('./testdir/nesteddir1/f', 'a')
    f1.write(gen_random_string_len(512))
    f1.close()
    walk.walk('./testdir', './dst', './log/log')
    f1 = open('./testdir/nesteddir1/f')
    f2 = open('./dst/nesteddir1/f')
    assert f1.read() == f2.read()
    f1.close()
    f2.close()
    rm_log_dir()



#def test_log_basic():
#    setup_dirs()
#    walk.walk('./testdir', './dst', './log/log')
#    with open('./log/log', 'r') as f:
#        i = len(f.readlines)
#    assert i == 1

