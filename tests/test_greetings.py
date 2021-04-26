import pytest

from my_module.greeting.greetings import Greetings


@pytest.fixture
def setup():
    under_test = Greetings()
    yield under_test


def test_greetings(setup):
    input_value = ['value1', 'value2']
    under_test = setup
    result = under_test.greet(input_value)
    assert result[0] == 'Hello, value1'
    assert result[1] == 'Hello, value2'
