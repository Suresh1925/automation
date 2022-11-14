# any pytest file name should start with test_
# pytest method name start with test
import pytest
@pytest.fixture()
def setup():
    print("I will be executing first")
    yield
    print("I will execute last")

@pytest.mark.smoke
def test_FirstProgram():
    print("hello world")


@pytest.mark.xfail
def test_SecondProgram():
    print("Good Morning")


