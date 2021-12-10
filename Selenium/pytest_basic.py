import pytest
def test_first():
    print("First test case and it's discovered")
    assert True

def test_second():
    print("Second Test Case")
    assert True

def test_third():
    print("Third Test Case")

class TestFourth:
    @staticmethod
    def test_fourth_a():
        print("Fourth TestCase a")
    @staticmethod
    def test_fourth_b():
        print("Fourth Testcase b")
