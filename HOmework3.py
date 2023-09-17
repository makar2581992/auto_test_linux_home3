# Задание 1.
#
# Условие:
# Дополнить проект фикстурой, которая после каждого шага теста дописывает в заранее созданный
# файл stat.txt строку вида:
# время, кол-во файлов из конфига, размер файла из конфига, статистика загрузки
# процессора из файла /proc/loadavg (можно писать просто всё содержимое этого файла).

import subprocess
import pytest as pytest

@pytest.fixture()
def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False

@pytest.fixture()
def test_stepl():
    # test1
    assert checkout("cd /home/user/tst; 7z a ../out/arx2", "Everything is Ok"), "test1 FAIL"

@pytest.fixture()
def test_step2():
    # test2
    assert checkout("cd /home/user/out; 7z e arx2.7z -o/home/zerg/folderl -y", "Everything is Ok"), "test2 FAIL"

@pytest.fixture()
def test_step3():
    # test3
    assert checkout("cd /home/user/out; 7z t arx2.7z", "Everything is Ok"), "test3 FAIL"

@pytest.fixture()
def test_step4():
    # test4
    assert checkout("cd /home/user/out; 7z t arx2.7z", "Everything is Ok"), "test4 FAIL"


@pytest.fixture()
def write_stat(file_path, info):
    with open(file_path, 'a') as file:
        file.write(info + '\n')

@pytest.fixture()
def test_fixture(tmp_path):
    stat_file = tmp_path / "stat.txt"
    stat_file.touch()

    test_stepl()
    write_stat(stat_file, "time1, files1, size1, stat1")

    test_step2()
    write_stat(stat_file, "time2, files2, size2, stat2")

    test_step3()
    write_stat(stat_file, "time3, files3, size3, stat3")

    test_step4()
    write_stat(stat_file, "time4, files4, size4, stat4")