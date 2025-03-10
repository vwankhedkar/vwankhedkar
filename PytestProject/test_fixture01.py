conftest.py

import pytest

def pytest_configure():
    pytest.weekday1 = ['mon', 'tue', 'wed']
    pytest.weekday2 = ['fri', 'sat', 'sun']

@pytest.fixture(scope="module")
def setup01(scope='module'):
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

@pytest.fixture()
def setup04(request):
    mon = getattr(request.module, "months")
    print("\n In Fixture04 \n")
    print("\n Fixture scope: " +str(request.scope))
    print("\n Calling function: " + str(request.function.__name__))
    print("\n Calling module: " + str(request.module.__name__))
    mon.append("April")
    yield mon

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
********************************************************
import pytest

def test_checkrequest(setup04):
    assert 1==1
********************************************************
import pytest

months = ["Jan", "Feb", 'Mar']
def test_checkrequest(setup04):
    assert "April" in setup04
    assert len(setup04) == 4
**********************************************************

import pytest

def pytest_configure():
    pytest.weekday1 = ['mon', 'tue', 'wed']
    pytest.weekday2 = ['fri', 'sat', 'sun']

@pytest.fixture(scope="module")
def setup01(scope='module'):
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

@pytest.fixture()
def setup04(request):
    mon = getattr(request.module, "months")
    print("\n In Fixture04 \n")
    print("\n Fixture scope: " +str(request.scope))
    print("\n Calling function: " + str(request.function.__name__))
    print("\n Calling module: " + str(request.module.__name__))
    mon.append("April")
    yield mon

@pytest.fixture()
def setup05():
    def get_Structure(name):
        if name == 'list':
            return [1, 2, 3]
        elif name == 'tuple':
            return (1, 3, 4)
    return get_Structure

*********************************************************************
import pytest

months = ["Jan", "Feb", 'Mar']
def test_checkrequest(setup04):
    assert "April" in setup04
    assert len(setup04) == 4

def test_fact_fixture(setup05):
    assert type(setup05('list')) == list
    assert type(setup05('tuple')) == tuple
