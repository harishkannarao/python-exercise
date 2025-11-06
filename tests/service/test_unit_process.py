import asyncio
from unittest.mock import MagicMock, AsyncMock

from assertpy import assert_that
from pytest_mock import MockerFixture

from app.service import process


def test_get_response_unit(mocker: MockerFixture) -> None:
    mock_get_response_from_endpoint: MagicMock = MagicMock()
    mocker.patch(
        "app.service.process.interface.get_response_from_endpoint",
        mock_get_response_from_endpoint,
    )

    expected: str = "test-response"
    mock_get_response_from_endpoint.return_value = expected

    input_url: str = "http://www.example.com"
    result: str = process.get_response(input_url)

    assert_that(result).is_equal_to(expected)

    assert len(mock_get_response_from_endpoint.call_args_list) == 1

    assert mock_get_response_from_endpoint.call_args.args == (input_url,)


def test_async_get_response_unit(mocker: MockerFixture) -> None:
    mock_get_response_from_endpoint: AsyncMock = AsyncMock()
    mocker.patch(
        "app.service.process.interface.async_get_response_from_endpoint",
        mock_get_response_from_endpoint,
    )

    expected: str = "test-response"
    mock_get_response_from_endpoint.return_value = expected

    input_url: str = "http://www.example.com"
    result: str = asyncio.run(process.async_get_response(input_url))

    assert_that(result).is_equal_to(expected)

    assert len(mock_get_response_from_endpoint.call_args_list) == 1

    assert mock_get_response_from_endpoint.call_args.args == (input_url,)
