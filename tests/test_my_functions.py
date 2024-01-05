import pytest
import src.my_functions as my_functions


def test_add1():
    pass


def test_add2():
    result = my_functions.add(number_one=1, number_two=2)
    assert result == 3


def test_add3():
    result = my_functions.add(number_one=1, number_two=2)
    assert result == 4


def test_divide():
    assert 5 == my_functions.divide(number_one=10, number_two=2)


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(number_one=10, number_two=0)
