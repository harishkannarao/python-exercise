import asyncio
from dataclasses import dataclass
from unittest.mock import MagicMock, AsyncMock

import pytest
from assertpy import assert_that

from app.external import interface
from pytest_mock import MockerFixture


@dataclass(frozen=True)
class Setup:
    mock_get: MagicMock
    mock_sleep: AsyncMock


@pytest.fixture
def setup(mocker: MockerFixture) -> Setup:
    mock_get: MagicMock = mocker.patch("app.external.interface.requests.get")
    mock_sleep: AsyncMock = mocker.patch("app.external.interface.asyncio.sleep")
    return Setup(mock_get=mock_get, mock_sleep=mock_sleep)


def test_get_response_from_endpoint(setup: Setup) -> None:
    expected: str = "test-response"
    mock_response: MagicMock = MagicMock()
    mock_response.text = expected
    setup.mock_get.return_value = mock_response

    input_url: str = "http://www.example.com"
    result: str = interface.get_response_from_endpoint(input_url)

    assert_that(result).is_equal_to(expected)

    assert len(setup.mock_get.call_args_list) == 1

    assert setup.mock_get.call_args.args == (input_url,)


def test_async_get_response_from_endpoint(setup: Setup) -> None:
    expected: str = "test-response"
    mock_response: MagicMock = MagicMock()
    mock_response.text = expected

    setup.mock_get.return_value = mock_response

    input_url: str = "http://www.example.com"
    result: str = asyncio.run(interface.async_get_response_from_endpoint(input_url))

    assert_that(result).is_equal_to(expected)

    assert len(setup.mock_get.call_args_list) == 1

    assert setup.mock_get.call_args.args == (input_url,)

    assert len(setup.mock_sleep.call_args_list) == 1
    assert setup.mock_sleep.call_args.args == (3,)
