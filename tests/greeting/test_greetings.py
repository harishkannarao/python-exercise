import asyncio
from dataclasses import dataclass

import pytest

from app.greeting.greetings import Greetings


@dataclass(frozen=True)
class Setup:
    under_test: Greetings


@pytest.fixture
def setup() -> Setup:
    return Setup(under_test=Greetings())


def test_greetings(setup: Setup):
    input_value = ["value1", "value2"]
    result = setup.under_test.greet(input_value)
    assert result[0] == "Hello, value1"
    assert result[1] == "Hello, value2"


def test_async_greetings(setup: Setup):
    input_value = ["value1", "value2"]
    result: list[str] = asyncio.run(setup.under_test.async_greet(input_value))
    assert result[0] == "Hello, value1"
    assert result[1] == "Hello, value2"
