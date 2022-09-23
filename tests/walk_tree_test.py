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

def delete_test_dirs():
    try:
        rm_test_dir()
    except FileNotFoundError:
        pass
    try:
        rm_dst_dir()
    except FileNotFoundError:
        pass

def setup_dirs():
    delete_test_dirs()
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
    delete_test_dirs()
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
    delete_test_dirs()
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
    delete_test_dirs()
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
    delete_test_dirs()
    rm_log_dir()

def test_big_files():
    setup_dirs()
    create_test_file_len('./testdir/nesteddir1/f', 171824)
    create_test_file_len('./testdir/nesteddir1/f1', 1421824)
    create_test_file_len('./testdir/nesteddir2/f', 178224)
    create_test_file_len('./testdir/nesteddir2/f1', 118224)
    walk.walk('./testdir', './dst', './log/log')

    assert os.stat('./testdir/nesteddir1/f').st_size == os.stat('./dst/nesteddir1/f').st_size

    assert os.stat('./testdir/nesteddir1/f1').st_size == os.stat('./dst/nesteddir1/f1').st_size

    assert os.stat('./testdir/nesteddir2/f').st_size == os.stat('./dst/nesteddir2/f').st_size

    assert os.stat('./testdir/nesteddir2/f1').st_size == os.stat('./dst/nesteddir2/f1').st_size


    delete_test_dirs()
    rm_log_dir()

def test_big_files_2():
    setup_dirs()
    create_test_file_len('./testdir/nesteddir1/f', 1721824)
    create_test_file_len('./testdir/nesteddir1/f1', 1421824)
    create_test_file_len('./testdir/nesteddir1/f2', 1421824)
    create_test_file_len('./testdir/nesteddir1/f3', 1421824)
    create_test_file_len('./testdir/nesteddir2/f', 1718124)
    create_test_file_len('./testdir/nesteddir2/f1', 118224)
    create_test_file_len('./testdir/nesteddir2/f2', 1428524)
    walk.walk('./testdir', './dst', './log/log')
    assert os.stat('./testdir/nesteddir1/f').st_size == os.stat('./dst/nesteddir1/f').st_size

    assert os.stat('./testdir/nesteddir1/f1').st_size == os.stat('./dst/nesteddir1/f1').st_size

    assert os.stat('./testdir/nesteddir1/f2').st_size == os.stat('./dst/nesteddir1/f2').st_size

    assert os.stat('./testdir/nesteddir1/f3').st_size == os.stat('./dst/nesteddir1/f3').st_size

    assert os.stat('./testdir/nesteddir2/f').st_size == os.stat('./dst/nesteddir2/f').st_size

    assert os.stat('./testdir/nesteddir2/f1').st_size == os.stat('./dst/nesteddir2/f1').st_size

    assert os.stat('./testdir/nesteddir2/f2').st_size == os.stat('./dst/nesteddir2/f2').st_size

    delete_test_dirs()
    rm_log_dir()

def test_big_files_3():
    setup_dirs()
    os.mkdir('./testdir/nesteddir1/n')
    create_test_file_len('./testdir/nesteddir1/f', 1721824)
    create_test_file_len('./testdir/nesteddir1/f1', 1421824)
    create_test_file_len('./testdir/nesteddir1/f2', 1421824)
    create_test_file_len('./testdir/nesteddir1/f3', 14218524)
    create_test_file_len('./testdir/nesteddir1/f4', 14218524)
    create_test_file_len('./testdir/nesteddir1/n/f', 14218524)
    create_test_file_len('./testdir/nesteddir1/n/f1', 14218524)
    create_test_file_len('./testdir/nesteddir1/n/f2', 14218524)
    create_test_file_len('./testdir/nesteddir2/f', 1718224)
    create_test_file_len('./testdir/nesteddir2/f1', 118224)
    create_test_file_len('./testdir/nesteddir2/f2', 1428524)
    walk.walk('./testdir', './dst', './log/log')
    assert os.stat('./testdir/nesteddir1/f').st_size == os.stat('./dst/nesteddir1/f').st_size

    assert os.stat('./testdir/nesteddir1/f1').st_size == os.stat('./dst/nesteddir1/f1').st_size

    assert os.stat('./testdir/nesteddir1/f2').st_size == os.stat('./dst/nesteddir1/f2').st_size

    assert os.stat('./testdir/nesteddir1/f3').st_size == os.stat('./dst/nesteddir1/f3').st_size

    assert os.stat('./testdir/nesteddir1/f4').st_size == os.stat('./dst/nesteddir1/f4').st_size

    assert os.stat('./testdir/nesteddir1/n/f').st_size == os.stat('./dst/nesteddir1/n/f').st_size

    assert os.stat('./testdir/nesteddir1/n/f1').st_size == os.stat('./dst/nesteddir1/n/f1').st_size
    assert os.stat('./testdir/nesteddir1/n/f2').st_size == os.stat('./dst/nesteddir1/n/f2').st_size

    assert os.stat('./testdir/nesteddir2/f').st_size == os.stat('./dst/nesteddir2/f').st_size

    assert os.stat('./testdir/nesteddir2/f1').st_size == os.stat('./dst/nesteddir2/f1').st_size

    assert os.stat('./testdir/nesteddir2/f2').st_size == os.stat('./dst/nesteddir2/f2').st_size

    delete_test_dirs()
    rm_log_dir()