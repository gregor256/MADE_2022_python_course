"""test"""
import pytest


def test_int():
    """test"""
    assert int(0) == 0
    assert int(0.1) == 0
    assert int(-0.1) == 0
    assert int(0.9) == 0
    assert int('0') == 0
    assert int(b'110', 2) == 6


def test_int_asserts():
    """test"""
    with pytest.raises(ValueError) as exc_info:
        int('s')
    assert str(exc_info.value) == "invalid literal for int() with base 10: 's'"

    with pytest.raises(ValueError) as exc_info:
        int('0.9')
    assert str(exc_info.value) == "invalid literal for int() with base 10: '0.9'"

    with pytest.raises(TypeError) as exc_info:
        int([1, 2, 3])
    assert str(exc_info.value) == "int() argument must be a string," \
                                  " a bytes-like object or a real number, not 'list'"
