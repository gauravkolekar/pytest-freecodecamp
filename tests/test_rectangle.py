import pytest
import math
import src.shapes as shapes


@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(length=10, width=2)


def test_area(my_rectangle):
    assert my_rectangle.area() == my_rectangle.length * my_rectangle.width


def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == (my_rectangle.length * 2) + (
        my_rectangle.width * 2
    )


def test_rectangle_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle
