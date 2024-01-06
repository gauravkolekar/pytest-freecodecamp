import pytest
import src.shapes as shapes


@pytest.mark.parametrize("side_length, expected_area", [(5, 25), (4, 16)])
def test_square_areas(side_length, expected_area):
    assert shapes.Square(side_length=side_length).area() == expected_area


@pytest.mark.parametrize("side_length, expected_perimeter", [(3, 12), (4, 16)])
def test_square_perimeters(side_length, expected_perimeter):
    assert shapes.Square(side_length=side_length).perimeter() == expected_perimeter
