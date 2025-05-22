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
**************************************************************************
import pytest

@pytest.fixture()
def setup_list():
    print("\n In Fixture \n")
    city = ['NewYork', 'London', 'Mumbai', 'Riyadh', 'Singapore', ]
    return city
def test_getitem(setup_list):
    print(setup_list[1::3])
    assert setup_list[2] == 'Mumbai'
    assert setup_list[0] == 'NewYork'
def myreverse(lst):
    lst.reverse()
    return lst
def test_reverslist(setup_list):
    print(setup_list[::2])
    assert setup_list[::2] == ['NewYork', 'Mumbai', 'Singapore']
    assert setup_list[::-1] == myreverse(setup_list)
(.venv) PS C:\Users\vwank\PycharmProjects\PythonProject4\pytest_topics> pytest -v -k fixture -s
=============================================================== test session starts ===============================================================
platform win32 -- Python 3.13.1, pytest-8.3.5, pluggy-1.5.0 -- C:\Trainings\RobotFramework\RobotFramework\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\vwank\PycharmProjects\PythonProject4
configfile: pytest.ini
collected 12 items / 10 deselected / 2 selected                                                                                                    

test_fixture.py::test_getitem 
 In Fixture

['London', 'Singapore']
PASSED
test_fixture.py::test_reverslist
 In Fixture

['NewYork', 'Mumbai', 'Singapore']
PASSED

======================================================== 2 passed, 10 deselected in 0.06s ========================================================= 
(.venv) PS C:\Users\vwank\PycharmProjects\PythonProject4\pytest_topics> 
