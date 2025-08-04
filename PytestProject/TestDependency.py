import pytest
class TestDepends:
    @pytest.mark.dependancy()
    def test_method1(self):
        print("Method-1 is called")
        assert 1+2 == 4
    @pytest.mark.dependency(depends = ["TestDepends::test_method1"])
    def test_method2(self):
        print("Method-2 is called")
    def test_method3(self):
        print("Method-3 is called")
class TestNew:
    @pytest.mark.dependency(depends = ["TestDepends::test_method1"])
    def test_method4(self):
        print("Method-4 is called")
(.venv) PS C:\Users\vwank\PycharmProjects\PytestJuly25\Pytest> pip install pytest-dependency  
(.venv) PS C:\Users\vwank\PycharmProjects\PytestJuly25\Pytest> pytest -v -s .\testDependency.py
============================================================ test session starts =============================================================
platform win32 -- Python 3.13.1, pytest-8.4.1, pluggy-1.6.0 -- C:\Users\vwank\PycharmProjects\PytestJuly25\.venv\Scripts\python.exe
cachedir: .pytest_cache
metadata: {'Python': '3.13.1', 'Platform': 'Windows-11-10.0.26100-SP0', 'Packages': {'pytest': '8.4.1', 'pluggy': '1.6.0'}, 'Plugins': {'dependency': '0.6.0', 'html': '4.1.1', 'metadata': '3.1.1', 'xdist': '3.8.0'}, 'JAVA_HOME': 'C:\\Program Files\\Java\\jdk-17'}
rootdir: C:\Users\vwank\PycharmProjects\PytestJuly25\Pytest
plugins: dependency-0.6.0, html-4.1.1, metadata-3.1.1, xdist-3.8.0
collected 4 items

testDependency.py::TestDepends::test_method1 Method-1 is called
FAILED
testDependency.py::TestDepends::test_method2 SKIPPED (test_method2 depends on TestDepends::test_method1)
testDependency.py::TestDepends::test_method3 Method-3 is called
PASSED
testDependency.py::TestNew::test_method4 SKIPPED (test_method4 depends on TestDepends::test_method1)

================================================================== FAILURES ================================================================== 
__________________________________________________________ TestDepends.test_method1 __________________________________________________________ 

self = <testDependency.TestDepends object at 0x000001C5ACACF390>

    @pytest.mark.dependancy()
    def test_method1(self):
        print("Method-1 is called")
>       assert 1+2 == 4
E       assert (1 + 2) == 4

testDependency.py:6: AssertionError
============================================================== warnings summary ============================================================== 
testDependency.py:3
  C:\Users\vwank\PycharmProjects\PytestJuly25\Pytest\testDependency.py:3: PytestUnknownMarkWarning: Unknown pytest.mark.dependancy - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.dependancy()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
========================================================== short test summary info =========================================================== 
FAILED testDependency.py::TestDepends::test_method1 - assert (1 + 2) == 4
============================================= 1 failed, 1 passed, 2 skipped, 1 warning in 0.10s ============================================== 
(.venv) PS C:\Users\vwank\PycharmProjects\PytestJuly25\Pytest>   
