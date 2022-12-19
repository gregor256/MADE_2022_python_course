"""test"""
import pytest


def test_partition():
    """test"""
    assert 'I love Python'.partition(' ') == ('I', ' ', 'love Python')
    assert 'I love Python'.partition('*') == ('I love Python', '', '')

    assert ''.partition(' ') == ('', '', '')
    assert ' '.partition(' ') == ('', ' ', '')


def test_int_asserts():
    """test"""
    with pytest.raises(TypeError) as exc_info:
        'I love Python'.partition()
    assert str(exc_info.value) == "str.partition() takes exactly one argument (0 given)"
