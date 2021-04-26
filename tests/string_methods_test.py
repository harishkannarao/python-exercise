import pytest


def test_upper():
    assert 'foo'.upper() == 'FOO'


def test_isupper():
    assert True == 'FOO'.isupper()
    assert False == 'foo'.isupper()


def test_split():
    s = 'hello world'
    assert s.split() == ['hello', 'world']
    with pytest.raises(TypeError) as result:
        s.split(2)
    assert str(result.value) == 'must be str or None, not int'
