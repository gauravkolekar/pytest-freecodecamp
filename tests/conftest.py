"""
conftest can be used to make all the fixtures global
"""
import pytest
import src.shapes as shapes


@pytest.fixture
def weird_rectangle():
    return shapes.Rectangle(length=2, width=8)
