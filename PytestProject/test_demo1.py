test_demo1.py
-------------
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

def test_m4():
    assert 100 == 100

def test_m5():
    assert True

test_demo2.py
------------
def test_m6():
    assert "vaishali" == "VAISHALI"

def test_m7():
    assert "vaishali" != "VAISHALI"

OUTPUT:
------

PS D:\pytestProject\nopCommerceApp\pytestsessions> py.test .\test_demo1.py
=============================================================== test session starts ===============================================================
platform win32 -- Python 3.11.4, pytest-7.4.0, pluggy-1.2.0
rootdir: D:\pytestProject\nopCommerceApp\pytestsessions
collected 5 items                                                                                                                                   

test_demo1.py F.F..                                                                                                                          [100%]

==================================================================== FAILURES ===================================================================== 
_____________________________________________________________________ test_m1 _____________________________________________________________________ 

    def test_m1():
        a=3
        b=4
        assert a+1 == b, "test failed"
>       assert a == b, "test failed as a is not equal to b"
E       AssertionError: test failed as a is not equal to b
E       assert 3 == 4

test_demo1.py:6: AssertionError
_____________________________________________________________________ test_m3 _____________________________________________________________________ 
    def test_m3():
>       assert False
E       assert False

test_demo1.py:13: AssertionError
============================================================= short test summary info ============================================================= 
FAILED test_demo1.py::test_m1 - AssertionError: test failed as a is not equal to b
FAILED test_demo1.py::test_m3 - assert False
=========================================================== 2 failed, 3 passed in 0.08s =========================================================== 
PS D:\pytestProject\nopCommerceApp\pytestsessions> py.test .\test_demo2.py
=============================================================== test session starts ===============================================================
platform win32 -- Python 3.11.4, pytest-7.4.0, pluggy-1.2.0
rootdir: D:\pytestProject\nopCommerceApp\pytestsessions
collected 2 items                                                                                                                                   

test_demo2.py F.                                                                                                                             [100%]

==================================================================== FAILURES ===================================================================== 
_____________________________________________________________________ test_m6 _____________________________________________________________________ 

    def test_m6():
>       assert "vaishali" == "VAISHALI"
E       AssertionError: assert 'vaishali' == 'VAISHALI'
E         - VAISHALI
E         + vaishali

test_demo2.py:2: AssertionError
============================================================= short test summary info ============================================================= 
FAILED test_demo2.py::test_m6 - AssertionError: assert 'vaishali' == 'VAISHALI'
=========================================================== 1 failed, 1 passed in 0.07s =========================================================== 
PS D:\pytestProject\nopCommerceApp\pytestsessions> 


