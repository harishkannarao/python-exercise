import asyncio
from unittest.mock import MagicMock, AsyncMock

from assertpy import assert_that

from app.external import interface
from pytest_mock import MockerFixture


def test_get_response_from_endpoint(mocker: MockerFixture) -> None:
    mock_get_response_from_endpoint: MagicMock = MagicMock()
    mock_response: MagicMock = MagicMock()
    mocker.patch(
        "app.external.interface.requests.get",
        mock_get_response_from_endpoint,
    )

    expected: str = "test-response"
    mock_get_response_from_endpoint.return_value = mock_response
    mock_response.text = expected

    input_url: str = "http://www.example.com"
    result: str = interface.get_response_from_endpoint(input_url)

    assert_that(result).is_equal_to(expected)

    assert len(mock_get_response_from_endpoint.call_args_list) == 1

    assert mock_get_response_from_endpoint.call_args.args == (input_url,)


def test_async_get_response_from_endpoint(mocker: MockerFixture) -> None:
    mock_get_response_from_endpoint: MagicMock = MagicMock()
    mock_response: MagicMock = MagicMock()
    mocker.patch(
        "app.external.interface.requests.get",
        mock_get_response_from_endpoint,
    )

    mock_sleep: AsyncMock = mocker.patch(
        "app.external.interface.asyncio.sleep", autospec=True
    )

    expected: str = "test-response"
    mock_get_response_from_endpoint.return_value = mock_response
    mock_response.text = expected

    input_url: str = "http://www.example.com"
    result: str = asyncio.run(interface.async_get_response_from_endpoint(input_url))

    assert_that(result).is_equal_to(expected)

    assert len(mock_get_response_from_endpoint.call_args_list) == 1

    assert mock_get_response_from_endpoint.call_args.args == (input_url,)

    assert len(mock_sleep.call_args_list) == 1
    assert mock_sleep.call_args.args == (3,)
