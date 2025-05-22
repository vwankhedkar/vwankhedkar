def test_a1():
    assert 4 != 3
def test_a2():
    assert 1
def test_a3():
    assert "abc" == 'abcd'
def test_a4():
    assert ((3-1)*4/2) == 4.0
def test_a5():
    assert 1 in divmod(9,5)
    assert 'put' not in 'this IS pytes'
    assert [1,2,4] == [1,2,4]
  (.venv) C:\Users\vwank\PycharmProjects\PythonProject4\pytest_topics> C:\Users\vwank\PycharmProjects\PythonProject4\.venv\Scripts\activate

(.venv) C:\Users\vwank\PycharmProjects\PythonProject4\pytest_topics>pytest
================================================= test session starts =================================================
platform win32 -- Python 3.12.7, pytest-8.3.5, pluggy-1.6.0
rootdir: C:\Users\vwank\PycharmProjects\PythonProject4\pytest_topics
collected 5 items

test_module01.py ..F..                                                                                           [100%]

====================================================== FAILURES =======================================================
_______________________________________________________ test_a3 _______________________________________________________

    def test_a3():
>       assert "abc" == 'abcd'
E       AssertionError: assert 'abc' == 'abcd'
E
E         - abcd
E         ?    -
E         + abc

test_module01.py:6: AssertionError
=============================================== short test summary info ===============================================
FAILED test_module01.py::test_a3 - AssertionError: assert 'abc' == 'abcd'
============================================= 1 failed, 4 passed in 0.07s =============================================

(.venv) C:\Users\vwank\PycharmProjects\PythonProject4\pytest_topics>       

******************************
(.venv) C:\Users\vwank\PycharmProjects\PythonProject4\pytest_topics>pytest -v
================================================= test session starts =================================================
platform win32 -- Python 3.12.7, pytest-8.3.5, pluggy-1.6.0 -- C:\Users\vwank\PycharmProjects\PythonProject4\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\vwank\PycharmProjects\PythonProject4\pytest_topics
collected 5 items

test_module01.py::test_a1 PASSED                                                                                 [ 20%]
test_module01.py::test_a2 PASSED                                                                                 [ 40%]
test_module01.py::test_a3 FAILED                                                                                 [ 60%]
test_module01.py::test_a4 PASSED                                                                                 [ 80%]
test_module01.py::test_a5 PASSED                                                                                 [100%]

====================================================== FAILURES =======================================================
_______________________________________________________ test_a3 _______________________________________________________

    def test_a3():
>       assert "abc" == 'abcd'
E       AssertionError: assert 'abc' == 'abcd'
E
E         - abcd
E         ?    -
E         + abc

test_module01.py:6: AssertionError
=============================================== short test summary info ===============================================
FAILED test_module01.py::test_a3 - AssertionError: assert 'abc' == 'abcd'
============================================= 1 failed, 4 passed in 0.05s =============================================

(.venv) C:\Users\vwank\PycharmProjects\PythonProject4\pytest_topics>

*******************************************
(.venv) C:\Users\vwank\PycharmProjects\PythonProject4\pytest_topics>pytest -v -k "a1"
================================================= test session starts =================================================
platform win32 -- Python 3.12.7, pytest-8.3.5, pluggy-1.6.0 -- C:\Users\vwank\PycharmProjects\PythonProject4\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\vwank\PycharmProjects\PythonProject4\pytest_topics
collected 5 items / 4 deselected / 1 selected

test_module01.py::test_a1 PASSED                                                                                 [100%]

=========================================== 1 passed, 4 deselected in 0.02s ===========================================

(.venv) C:\Users\vwank\PycharmProjects\PythonProject4\pytest_topics>
**********************************************

  # pytest -v -k "a1 and a2"  ==> Won't have any test with both a1 and a2 in it
  
(.venv) C:\Users\vwank\PycharmProjects\PythonProject4\pytest_topics>pytest -v -k "a1 or a2"
================================================= test session starts =================================================
platform win32 -- Python 3.12.7, pytest-8.3.5, pluggy-1.6.0 -- C:\Users\vwank\PycharmProjects\PythonProject4\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\vwank\PycharmProjects\PythonProject4\pytest_topics
collected 5 items / 3 deselected / 2 selected

test_module01.py::test_a1 PASSED                                                                                 [ 50%]
test_module01.py::test_a2 PASSED                                                                                 [100%]

=========================================== 2 passed, 3 deselected in 0.01s ===========================================

(.venv) C:\Users\vwank\PycharmProjects\PythonProject4\pytest_topics>
*****************************************
(.venv) C:\Users\vwank\PycharmProjects\PythonProject4\pytest_topics>pytest -v --collect-only
================================================= test session starts =================================================
platform win32 -- Python 3.12.7, pytest-8.3.5, pluggy-1.6.0 -- C:\Users\vwank\PycharmProjects\PythonProject4\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\vwank\PycharmProjects\PythonProject4\pytest_topics
collected 5 items

<Package pytest_topics>
  <Module test_module01.py>
    <Function test_a1>
    <Function test_a2>
    <Function test_a3>
    <Function test_a4>
    <Function test_a5>

============================================= 5 tests collected in 0.01s ==============================================

(.venv) C:\Users\vwank\PycharmProjects\PythonProject4\pytest_topics>
***********************************
(.venv) C:\Users\vwank\PycharmProjects\PythonProject4\pytest_topics>pytest -v --collect-only -k "a1"
================================================= test session starts =================================================
platform win32 -- Python 3.12.7, pytest-8.3.5, pluggy-1.6.0 -- C:\Users\vwank\PycharmProjects\PythonProject4\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\vwank\PycharmProjects\PythonProject4\pytest_topics
collected 5 items / 4 deselected / 1 selected

<Package pytest_topics>
  <Module test_module01.py>
    <Function test_a1>

===================================== 1/5 tests collected (4 deselected) in 0.02s =====================================

(.venv) C:\Users\vwank\PycharmProjects\PythonProject4\pytest_topics>
*************************************************
(.venv) C:\Users\vwank\PycharmProjects\PythonProject4\pytest_topics>pytest -v --exitfirst
================================================= test session starts =================================================
platform win32 -- Python 3.12.7, pytest-8.3.5, pluggy-1.6.0 -- C:\Users\vwank\PycharmProjects\PythonProject4\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\vwank\PycharmProjects\PythonProject4\pytest_topics
collected 5 items

test_module01.py::test_a1 PASSED                                                                                 [ 20%]
test_module01.py::test_a2 PASSED                                                                                 [ 40%]
test_module01.py::test_a3 FAILED                                                                                 [ 60%]

====================================================== FAILURES =======================================================
_______________________________________________________ test_a3 _______________________________________________________

    def test_a3():
>       assert "abc" == 'abcd'
E       AssertionError: assert 'abc' == 'abcd'
E
E         - abcd
E         ?    -
E         + abc

test_module01.py:6: AssertionError
=============================================== short test summary info ===============================================
FAILED test_module01.py::test_a3 - AssertionError: assert 'abc' == 'abcd'
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! stopping after 1 failures !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
============================================= 1 failed, 2 passed in 0.10s =============================================

(.venv) C:\Users\vwank\PycharmProjects\PythonProject4\pytest_topics>
************************************************
pytest.ini
[pytest]
markers =
    smoke: smoke tests
    sanity: sanity test
    str
    strtest

test_markers.py
import pytest
pytestmark = [pytest.mark.smoke, pytest.mark.strtest]
@pytest.mark.sanity
def test_str01():
    num = 9/4
    s1 = 'I like ' + 'pytest automation'
    assert str(num) == '2.25'
    assert s1 == 'I like pytest automation'
    assert s1 + str(num) == 'I like pytest automation2.25'

@pytest.mark.sanity
def test_str02():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert len(letters) == 26
def test_str03():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert letters[0] == 'a'
    assert letters[-1] == 'z' == letters[25]
@pytest.mark.sanity
@pytest.mark.strtest
def test_strslice():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert letters[:] == letters
    assert letters[10:] == 'letters' == 'klmnopqrstuvwxyz'
    assert letters[-3] == 'xyz'
    assert letters[:21:5] == 'afkpu'

def test_strsplit():
    s1 = 'Python,Pytest and Automation'
    l1 = ['Python,Pytest', 'and', 'Automation']
    l2 = ['Python', 'Pytest and Automation']

(.venv) PS C:\Users\vwank\PycharmProjects\PythonProject4\pytest_topics> pytest -v -m "sanity or str"
=============================================================== test session starts ===============================================================
platform win32 -- Python 3.13.1, pytest-8.3.5, pluggy-1.5.0 -- C:\Trainings\RobotFramework\RobotFramework\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\vwank\PycharmProjects\PythonProject4
configfile: pytest.ini
collected 10 items / 7 deselected / 3 selected                                                                                                     

test_markers.py::test_str01 PASSED                                                                                                           [ 33%]
test_markers.py::test_str02 PASSED                                                                                                           [ 66%] 
test_markers.py::test_strslice FAILED                                                                                                        [100%]

==================================================================== FAILURES ===================================================================== 
__________________________________________________________________ test_strslice __________________________________________________________________ 

    @pytest.mark.sanity
    @pytest.mark.strtest
    def test_strslice():
        letters = 'abcdefghijklmnopqrstuvwxyz'
        assert letters[:] == letters
>       assert letters[10:] == 'letters' == 'klmnopqrstuvwxyz'
E       AssertionError: assert 'klmnopqrstuvwxyz' == 'letters'
E
E         - letters
E         + klmnopqrstuvwxyz

test_markers.py:24: AssertionError
============================================================= short test summary info ============================================================= 
FAILED test_markers.py::test_strslice - AssertionError: assert 'klmnopqrstuvwxyz' == 'letters'
==================================================== 1 failed, 2 passed, 7 deselected in 0.10s ==================================================== 
(.venv) PS C:\Users\vwank\PycharmProjects\PythonProject4\pytest_topics> 

(.venv) PS C:\Users\vwank\PycharmProjects\PythonProject4\pytest_topics> pytest -v --maxfail=2       
=============================================================== test session starts ===============================================================
platform win32 -- Python 3.13.1, pytest-8.3.5, pluggy-1.5.0 -- C:\Trainings\RobotFramework\RobotFramework\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\vwank\PycharmProjects\PythonProject4
configfile: pytest.ini
collected 10 items                                                                                                                                 

test_markers.py::test_str01 PASSED                                                                                                           [ 10%]
test_markers.py::test_str02 PASSED                                                                                                           [ 20%] 
test_markers.py::test_str03 FAILED                                                                                                           [ 30%]
test_markers.py::test_strslice FAILED                                                                                                        [ 40%] 

==================================================================== FAILURES ===================================================================== 
___________________________________________________________________ test_str03 ____________________________________________________________________ 

    def test_str03():
        letters = 'abcdefghijklmnopqrstuvwxyz'
        assert letters[0] == 'a'
>       assert letters[-1] == 'z' == letters[251]
E       IndexError: string index out of range

test_markers.py:18: IndexError
__________________________________________________________________ test_strslice __________________________________________________________________ 

    @pytest.mark.sanity
    @pytest.mark.strtest
    def test_strslice():
        letters = 'abcdefghijklmnopqrstuvwxyz'
        assert letters[:] == letters
>       assert letters[10:] == 'letters' == 'klmnopqrstuvwxyz'
E       AssertionError: assert 'klmnopqrstuvwxyz' == 'letters'
E
E         - letters
E         + klmnopqrstuvwxyz

test_markers.py:24: AssertionError
============================================================= short test summary info ============================================================= 
FAILED test_markers.py::test_str03 - IndexError: string index out of range
FAILED test_markers.py::test_strslice - AssertionError: assert 'klmnopqrstuvwxyz' == 'letters'
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! stopping after 2 failures !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 
=========================================================== 2 failed, 2 passed in 0.13s =========================================================== 
(.venv) PS C:\Users\vwank\PycharmProjects\PythonProject4\pytest_topics> 
