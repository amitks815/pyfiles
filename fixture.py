import pytest

@pytest.fixture
def hi_fixture():
    """
    will use as as small part of  setup and teardown method  
    """
    print("fixture is working fine ...")
    yield
    print("fixture checking done !")

def test_hello_fixture(hi_fixture): # function call first fixture then goes to inside .
    print("val")


