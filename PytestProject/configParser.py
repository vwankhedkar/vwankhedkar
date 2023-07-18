test_cases.py

import pytest

def calculate_sum(a, b):
    return a + b

def test_sum(test_cases):
    for case_name, case_data in test_cases.items():
        input_data = case_data["input"]
        expected_output = int(case_data["expected_output"])

        inputs = [int(x.strip()) for x in input_data.split(",")]
        result = calculate_sum(*inputs)

        assert result == expected_output, f"Test case {case_name} failed"

pytest.ini

[test_case_1]
input: 1, 2
expected_output: 3

[test_case_2]
input: 4, 5
expected_output: 9

conftest.py

import pytest
from configparser import ConfigParser

@pytest.fixture(scope="module")
def test_cases(request):
    config = ConfigParser()
    config.read("pytest.ini")

    sections = config.sections()

    return {section: config[section] for section in sections}

OUTPUT:

PS D:\pytestProject\nopCommerceApp\pytestconfig> pytest -v
=============================================================== test session starts ===============================================================
platform win32 -- Python 3.11.4, pytest-7.4.0, pluggy-1.2.0 -- C:\Python311\python.exe
cachedir: .pytest_cache
rootdir: D:\pytestProject\nopCommerceApp\pytestconfig
configfile: pytest.ini
collected 1 item                                                                                                                                    

test_cases.py::test_sum PASSED                                                                                                               [100%]

================================================================ 1 passed in 0.02s ================================================================ 
PS D:\pytestProject\nopCommerceApp\pytestconfig> 


