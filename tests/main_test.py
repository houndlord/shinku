import main
import pytest
import walk_tree_test


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
