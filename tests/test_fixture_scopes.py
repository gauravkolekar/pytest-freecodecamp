import pytest
from src.fixture_scopes import Calculate

# comment fixtures to test all things out
@pytest.fixture
def calculate_instance():
    print("Setup...\n")
    yield Calculate()
    print("Teardown...\n")

@pytest.fixture(scope="session")
def calculate_instance2():
    print("Setup...\n")
    yield Calculate()
    print("Teardown...\n")

# def test_square(calculate_instance):
#     assert calculate_instance.square(5) == 25


def test_square2(calculate_instance2):
    assert calculate_instance2.square(2.) == 4.

def test_square3(calculate_instance2):
    assert calculate_instance2.square(2) == 4