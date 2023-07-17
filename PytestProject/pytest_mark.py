import pytest
@pytest.mark.login
def test_m1():
    a=3
    b=4
    assert a+1 == b, "test failed"
    assert a == b, "test failed as a is not equal to b"

def test_m2():
    name = "Selenium"
    assert name.upper() == "SELENIUM"

@pytest.mark.login
def test_m3():
    assert False

@pytest.mark.login
def test_m4():
    assert 100 == 100

def test_m5():
    assert True

def test_m6():
    assert "vaishali" == "VAISHALI"

OUTPUT:
------
PS D:\pytestProject\nopCommerceApp\pytestsessions> py.test .\test_demo1.py -m login


PS D:\pytestProject\nopCommerceApp\pytestsessions> py.test -m login
=============================================================== test session starts ===============================================================
platform win32 -- Python 3.11.4, pytest-7.4.0, pluggy-1.2.0
rootdir: D:\pytestProject\nopCommerceApp\pytestsessions
collected 13 items / 10 deselected / 3 selected

test_demo1.py FF.                                                                                                                            [100%]

==================================================================== FAILURES ===================================================================== 
_____________________________________________________________________ test_m1 _____________________________________________________________________ 

    @pytest.mark.login
    def test_m1():
        a=3
        b=4
        assert a+1 == b, "test failed"
>       assert a == b, "test failed as a is not equal to b"
E       AssertionError: test failed as a is not equal to b
E       assert 3 == 4

test_demo1.py:7: AssertionError
_____________________________________________________________________ test_m3 _____________________________________________________________________ 

    @pytest.mark.login
    def test_m3():
>       assert False
E       assert False

test_demo1.py:15: AssertionError
================================================================ warnings summary ================================================================= 
test_demo1.py:2
  D:\pytestProject\nopCommerceApp\pytestsessions\test_demo1.py:2: PytestUnknownMarkWarning: Unknown pytest.mark.login - is this a typo?  You can reg
ister custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.login

test_demo1.py:13
  D:\pytestProject\nopCommerceApp\pytestsessions\test_demo1.py:13: PytestUnknownMarkWarning: Unknown pytest.mark.login - is this a typo?  You can re
gister custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.login

test_demo1.py:17
  D:\pytestProject\nopCommerceApp\pytestsessions\test_demo1.py:17: PytestUnknownMarkWarning: Unknown pytest.mark.login - is this a typo?  You can re
gister custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.login

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
============================================================= short test summary info ============================================================= 
FAILED test_demo1.py::test_m1 - AssertionError: test failed as a is not equal to b
FAILED test_demo1.py::test_m3 - assert False
============================================= 2 failed, 1 passed, 10 deselected, 3 warnings in 0.17s ============================================== 
PS D:\pytestProject\nopCommerceApp\pytestsessions> 
