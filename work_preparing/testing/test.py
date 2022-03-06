import pytest


def division(a, b):
    return a / b


@pytest.mark.parametrize("a, b, expected_value", [(10, 2, 5), (1, 5, 0.2), (5, 2, 2.5), (3, 3, 1)])
def test_division_first(a, b, expected_value):
    assert division(a, b) == expected_value

def test_division_bt_zero():
    with pytest.raises(ZeroDivisionError):
        division(1, 0)


def test_division_type_error():
    with pytest.raises(TypeError):
        division("1", "0")