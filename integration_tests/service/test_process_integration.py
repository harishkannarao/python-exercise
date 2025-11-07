import asyncio
from dataclasses import dataclass
from unittest.mock import MagicMock, AsyncMock

import pytest
from assertpy import assert_that
from pytest_mock import MockerFixture

from app.service import process


@dataclass(frozen=True)
class MockHolder:
    mock_get: MagicMock
    mock_sleep: AsyncMock


@pytest.fixture
def mock_holder(mocker: MockerFixture):
    mock_get: MagicMock = mocker.patch("app.external.interface.requests.get")
    mock_sleep: AsyncMock = mocker.patch("app.external.interface.asyncio.sleep")
    return MockHolder(mock_get=mock_get, mock_sleep=mock_sleep)


def test_get_response_integration(mock_holder: MockHolder) -> None:
    expected: str = "test-response"
    mock_response: MagicMock = MagicMock()
    mock_response.text = expected
    mock_holder.mock_get.return_value = mock_response

    input_url: str = "http://www.example.com"
    result: str = process.get_response(input_url)

    assert_that(result).is_equal_to(expected)

    assert len(mock_holder.mock_get.call_args_list) == 1

    assert mock_holder.mock_get.call_args.args == (input_url,)


def test_async_get_response_integration(mock_holder: MockHolder) -> None:
    expected: str = "test-response"
    mock_response: MagicMock = MagicMock()
    mock_response.text = expected

    mock_holder.mock_get.return_value = mock_response

    input_url: str = "http://www.example.com"
    result: str = asyncio.run(process.async_get_response(input_url))

    assert_that(result).is_equal_to(expected)

    assert len(mock_holder.mock_get.call_args_list) == 1

    assert mock_holder.mock_get.call_args.args == (input_url,)

    assert len(mock_holder.mock_sleep.call_args_list) == 1
    assert mock_holder.mock_sleep.call_args.args == (3,)
