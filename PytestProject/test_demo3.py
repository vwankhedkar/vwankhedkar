import pytest
def test_m1():
    a=3
    b=4
    assert a+1 == b, "test failed"
    assert a == b, "test failed as a is not equal to b"

def test_m2():
    name = "Selenium"
    assert name.upper() == "SELENIUM"

def test_m3():
    assert False

def test_login():
    assert "admin" == "admin"

OUTPUT :-
------
PS D:\pytestProject\nopCommerceApp\pytestsessions> py.test -k login -v
=============================================================== test session starts ===============================================================
platform win32 -- Python 3.11.4, pytest-7.4.0, pluggy-1.2.0 -- C:\Python311\python.exe
cachedir: .pytest_cache
rootdir: D:\pytestProject\nopCommerceApp\pytestsessions
collected 11 items / 10 deselected / 1 selected                                                                                                     

test_demo3.py::test_login PASSED                                                                                                             [100%] 

======================================================== 1 passed, 10 deselected in 0.03s ========================================================= 
PS D:\pytestProject\nopCommerceApp\pytestsessions> 

test_demo2.py:
-------------
def test_m6():
    assert "vaishali" == "VAISHALI"

def test_m7():
    assert "vaishali" != "VAISHALI"

def test_login_FB():
    assert "admin" == "admin123"

OUTPUT:
------
PS D:\pytestProject\nopCommerceApp\pytestsessions> py.test -k login -v
=============================================================== test session starts ===============================================================
platform win32 -- Python 3.11.4, pytest-7.4.0, pluggy-1.2.0 -- C:\Python311\python.exe
cachedir: .pytest_cache
rootdir: D:\pytestProject\nopCommerceApp\pytestsessions
collected 12 items / 10 deselected / 2 selected

test_demo2.py::test_login_FB FAILED                                                                                                          [ 50%]
test_demo3.py::test_login PASSED                                                                                                             [100%] 

==================================================================== FAILURES ===================================================================== 
__________________________________________________________________ test_login_FB __________________________________________________________________ 

    def test_login_FB():
>       assert "admin" == "admin123"
E       AssertionError: assert 'admin' == 'admin123'
E         - admin123
E         ?      ---
E         + admin

test_demo2.py:8: AssertionError
============================================================= short test summary info ============================================================= 
FAILED test_demo2.py::test_login_FB - AssertionError: assert 'admin' == 'admin123'
=================================================== 1 failed, 1 passed, 10 deselected in 0.10s ==================================================== 
PS D:\pytestProject\nopCommerceApp\pytestsessions> 
