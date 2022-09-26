import main
import pytest
import walk_tree_test
import os


def test_not_existed_dirs():
    with pytest.raises(SystemExit) as e:
        r = main.check_path_existence('dasd', 'dad', '4343')
        assert e.type == SystemExit
        assert e.value.code == 1


def test_full_basic():
    walk_tree_test.setup_dirs()
    main.replicate('./testdir', './dst', './log/log')
    f1 = open('./testdir/f')
    f2 = open('./dst/f')
    assert f1.read() == f2.read()
    f1.close()
    f2.close()
    walk_tree_test.delete_test_dirs()
    walk_tree_test.rm_log_dir()


def test_full_nested():
    walk_tree_test.setup_dirs()
    walk_tree_test.create_test_file('./testdir/nesteddir1/f')
    main.replicate('./testdir', './dst', './log/log')
    f1 = open('./testdir/nesteddir1/f')
    f2 = open('./dst/nesteddir1/f')
    assert f1.read() == f2.read()
    f1.close()
    f2.close()
    walk_tree_test.delete_test_dirs()
    walk_tree_test.rm_log_dir()


def test_file_change_basic():
    walk_tree_test.setup_dirs()
    main.replicate('./testdir', './dst', './log/log')
    f1 = open('./testdir/f', 'a')
    f1.write(walk_tree_test.gen_random_string_len(512))
    f1.close()
    main.replicate('./testdir', './dst', './log/log')
    f1 = open('./testdir/f')
    f2 = open('./dst/f')
    assert f1.read() == f2.read()
    f1.close()
    f2.close()
    walk_tree_test.delete_test_dirs()
    walk_tree_test.rm_log_dir()


def test_walk_file_change_nested():
    walk_tree_test.setup_dirs()
    walk_tree_test.create_test_file('./testdir/nesteddir1/f')
    main.replicate('./testdir', './dst', './log/log')
    f1 = open('./testdir/nesteddir1/f', 'a')
    f1.write(walk_tree_test.gen_random_string_len(512))
    f1.close()
    main.replicate('./testdir', './dst', './log/log')
    f1 = open('./testdir/nesteddir1/f')
    f2 = open('./dst/nesteddir1/f')
    assert f1.read() == f2.read()
    f1.close()
    f2.close()
    walk_tree_test.delete_test_dirs()
    walk_tree_test.rm_log_dir()



def test_big_files():
    walk_tree_test.setup_dirs()
    walk_tree_test.create_test_file_len('./testdir/nesteddir1/f', 171824)
    walk_tree_test.create_test_file_len('./testdir/nesteddir1/f1', 1421824)
    walk_tree_test.create_test_file_len('./testdir/nesteddir2/f', 178224)
    walk_tree_test.create_test_file_len('./testdir/nesteddir2/f1', 118224)
    main.replicate('./testdir', './dst', './log/log')

    assert os.stat('./testdir/nesteddir1/f').st_size == os.stat(
        './dst/nesteddir1/f').st_size

    assert os.stat('./testdir/nesteddir1/f1').st_size == os.stat(
        './dst/nesteddir1/f1').st_size

    assert os.stat('./testdir/nesteddir2/f').st_size == os.stat(
        './dst/nesteddir2/f').st_size

    assert os.stat('./testdir/nesteddir2/f1').st_size == os.stat(
        './dst/nesteddir2/f1').st_size

    walk_tree_test.delete_test_dirs()
    walk_tree_test.rm_log_dir()


def test_big_files_2():
    walk_tree_test.setup_dirs()
    walk_tree_test.create_test_file_len('./testdir/nesteddir1/f', 1721824)
    walk_tree_test.create_test_file_len('./testdir/nesteddir1/f1', 1421824)
    walk_tree_test.create_test_file_len('./testdir/nesteddir1/f2', 1421824)
    walk_tree_test.create_test_file_len('./testdir/nesteddir1/f3', 1421824)
    walk_tree_test.create_test_file_len('./testdir/nesteddir2/f', 1718124)
    walk_tree_test.create_test_file_len('./testdir/nesteddir2/f1', 118224)
    walk_tree_test.create_test_file_len('./testdir/nesteddir2/f2', 1428524)
    main.replicate('./testdir', './dst', './log/log')
    assert os.stat('./testdir/nesteddir1/f').st_size == os.stat(
        './dst/nesteddir1/f').st_size

    assert os.stat('./testdir/nesteddir1/f1').st_size == os.stat(
        './dst/nesteddir1/f1').st_size

    assert os.stat('./testdir/nesteddir1/f2').st_size == os.stat(
        './dst/nesteddir1/f2').st_size

    assert os.stat('./testdir/nesteddir1/f3').st_size == os.stat(
        './dst/nesteddir1/f3').st_size

    assert os.stat('./testdir/nesteddir2/f').st_size == os.stat(
        './dst/nesteddir2/f').st_size

    assert os.stat('./testdir/nesteddir2/f1').st_size == os.stat(
        './dst/nesteddir2/f1').st_size

    assert os.stat('./testdir/nesteddir2/f2').st_size == os.stat(
        './dst/nesteddir2/f2').st_size

    walk_tree_test.delete_test_dirs()
    walk_tree_test.rm_log_dir()


def test_big_files_3():
    walk_tree_test.setup_dirs()
    os.mkdir('./testdir/nesteddir1/n')
    walk_tree_test.create_test_file_len('./testdir/nesteddir1/f', 1721824)
    walk_tree_test.create_test_file_len('./testdir/nesteddir1/f1', 1421824)
    walk_tree_test.create_test_file_len('./testdir/nesteddir1/f2', 1421824)
    walk_tree_test.create_test_file_len('./testdir/nesteddir1/f3', 14218524)
    walk_tree_test.create_test_file_len('./testdir/nesteddir1/f4', 14218524)
    walk_tree_test.create_test_file_len('./testdir/nesteddir1/n/f', 14218524)
    walk_tree_test.create_test_file_len('./testdir/nesteddir1/n/f1', 14218524)
    walk_tree_test.create_test_file_len('./testdir/nesteddir1/n/f2', 14218524)
    walk_tree_test.create_test_file_len('./testdir/nesteddir2/f', 1718224)
    walk_tree_test.create_test_file_len('./testdir/nesteddir2/f1', 118224)
    walk_tree_test.create_test_file_len('./testdir/nesteddir2/f2', 1428524)
    main.replicate('./testdir', './dst', './log/log')
    assert os.stat('./testdir/nesteddir1/f').st_size == os.stat(
        './dst/nesteddir1/f').st_size

    assert os.stat('./testdir/nesteddir1/f1').st_size == os.stat(
        './dst/nesteddir1/f1').st_size

    assert os.stat('./testdir/nesteddir1/f2').st_size == os.stat(
        './dst/nesteddir1/f2').st_size

    assert os.stat('./testdir/nesteddir1/f3').st_size == os.stat(
        './dst/nesteddir1/f3').st_size

    assert os.stat('./testdir/nesteddir1/f4').st_size == os.stat(
        './dst/nesteddir1/f4').st_size

    assert os.stat('./testdir/nesteddir1/n/f').st_size == os.stat(
        './dst/nesteddir1/n/f').st_size

    assert os.stat('./testdir/nesteddir1/n/f1').st_size == os.stat(
        './dst/nesteddir1/n/f1').st_size
    assert os.stat('./testdir/nesteddir1/n/f2').st_size == os.stat(
        './dst/nesteddir1/n/f2').st_size

    assert os.stat('./testdir/nesteddir2/f').st_size == os.stat(
        './dst/nesteddir2/f').st_size

    assert os.stat('./testdir/nesteddir2/f1').st_size == os.stat(
        './dst/nesteddir2/f1').st_size

    assert os.stat('./testdir/nesteddir2/f2').st_size == os.stat(
        './dst/nesteddir2/f2').st_size

    walk_tree_test.delete_test_dirs()
    walk_tree_test.rm_log_dir()


def test_perf():
    main.replicate('/home/houndlord/Downloads/',  '/home/houndlord/dd', '/home/houndlord/log')
"""
"""
def test_perms():
    walk_tree_test.setup_dirs()
    os.chmod('./testdir', 15384)
    main.replicate('./testdir', './dst', './log/log')
    f1 = open('./testdir/f')
    f2 = open('./dst/f')
    assert f1.read() == f2.read()
    f1.close()
    f2.close()
    walk_tree_test.delete_test_dirs()
    walk_tree_test.rm_log_dir()



def test_perms_basic():
    with pytest.raises(SystemExit) as e:
        walk_tree_test.setup_dirs()
        os.chmod('./testdir', 16384)
        r = main.replicate('./testdir', './dst', './log/log')
        assert e.type == SystemExit
        assert e.value.code == 1
        os.chmod('./testdir', 16877)
        walk_tree_test.delete_test_dirs()
        walk_tree_test.rm_log_dir()
