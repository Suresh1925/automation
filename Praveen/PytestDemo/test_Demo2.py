import pytest as pytest


@pytest.mark.smoke
def test_ThirdProgram():
    message="Hello"
    assert message == "Hi", "Test failed because string is not matching"