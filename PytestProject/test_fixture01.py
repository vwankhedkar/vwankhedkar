conftest.py

import pytest

def pytest_configure():
    pytest.weekday1 = ['mon', 'tue', 'wed']
    pytest.weekday2 = ['fri', 'sat', 'sun']

@pytest.fixture(scope="module")
def setup01():
    wk = pytest.weekday1.copy()
    wk.append('thur')
    yield wk
    print("\n Fixture setup closing")
    pytest.weekday1.pop()

@pytest.fixture()
def setup02():
    wk2 = pytest.weekday2.copy()
    wk2.insert(0,'thur')
    yield wk2
**********************************************************
test_fixture01.py
import pytest

def test_delItem(setup01):
    del setup01[-1]
    print(setup01)
    assert setup01 == pytest.weekday1

def test_removeItem(setup02):
    print(setup02)
    setup02.remove('thur')
    assert setup02 == pytest.weekday2

(.venv) PS C:\Users\vwank\PycharmProjects\PythonProject3> pytest -v -k test_fixture03 --setup-show


