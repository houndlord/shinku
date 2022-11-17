import random
import string
from utils import walk
import shutil
import os
import pytest
import sys


def gen_random_string():
    return ''.join(
        random.choice(string.ascii_letters)
        for i in range(random.randrange(0, 1000)))


def gen_random_string_len(length):
    return ''.join(random.choice(string.ascii_letters) for i in range(length))


def create_test_dir():
    try:
        os.mkdir('./testdir')
        os.mkdir('./testdir/nesteddir1')
        os.mkdir('./testdir/nesteddir2')
    except FileExistsError:
        rm_test_dir()
        create_test_dir()


def rm_test_dir():
    os.chmod('./testdir', 16877)
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


def test_dir_creation():
    setup_dirs()
    walk.walk('./testdir', './dst', './log/log')
    assert os.stat('./testdir/nesteddir1').st_size == os.stat(
        './dst/nesteddir1').st_size
    delete_test_dirs()
    rm_log_dir()


def test_backwalk_basic():
    setup_dirs()
    walk.walk('./testdir', './dst', './log/log')
    os.rmdir('./testdir/nesteddir1')
    walk.backwalk('./testdir', './dst', './log/log')
    assert len(os.listdir('./dst')) == 2
    delete_test_dirs()
    rm_log_dir()


def test_backwalk_nested():
    setup_dirs()
    create_test_file('./testdir/nesteddir1/f')
    walk.walk('./testdir', './dst', './log/log')
    os.remove('./testdir/nesteddir1/f')
    walk.backwalk('./testdir', './dst', './log/log')
    assert len(os.listdir('./dst/nesteddir1')) == 0
    delete_test_dirs()
    rm_log_dir()


if sys.platform.startswith('win'):
    pass
else:

    def test_perms_basic():
        with pytest.raises(SystemExit) as e:
            setup_dirs()
            os.chmod('./testdir', 16384)
            r = walk.walk('./testdir', './dst', './log/log')
            assert e.type == SystemExit
            assert e.value.code == 1
            os.chmod('./testdir', 16877)
            delete_test_dirs()
            rm_log_dir()

    def test_perms_backwalk_basic():
        with pytest.raises(SystemExit) as e:
            setup_dirs()
            os.chmod('./testdir', 16384)
            r = walk.backwalk('./testdir', './dst', './log/log')
            assert e.type == SystemExit
            assert e.value.code == 1
            os.chmod('./testdir', 16877)
            delete_test_dirs()
            rm_log_dir()

    def test_walk_perms():
        with pytest.raises(SystemExit) as e:
            setup_dirs()
            create_test_file('./testdir/f')
            os.chmod('./testdir/f', 16384)
            r = walk.walk('./testdir', './dst', './log/log')
            assert e.type == SystemExit
            assert e.value.code == 1
            os.chmod('./testdir/f', 16877)
            delete_test_dirs()
            rm_log_dir()
