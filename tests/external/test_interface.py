from unittest.mock import MagicMock

import pytest
from assertpy import assert_that

from app.external import interface
from tests.conftest import InterfaceSetup


def test_get_response_from_endpoint(interface_test_setup: InterfaceSetup) -> None:
    expected: str = "test-response"
    mock_response: MagicMock = MagicMock()
    mock_response.text = expected
    interface_test_setup.mock_get.return_value = mock_response

    input_url: str = "http://www.example.com"
    result: str = interface.get_response_from_endpoint(input_url)

    assert_that(result).is_equal_to(expected)

    assert len(interface_test_setup.mock_get.call_args_list) == 1

    assert interface_test_setup.mock_get.call_args.args == (input_url,)


@pytest.mark.asyncio
async def test_async_get_response_from_endpoint(
    interface_test_setup: InterfaceSetup,
) -> None:
    expected: str = "test-response"
    mock_response: MagicMock = MagicMock()
    mock_response.text = expected

    interface_test_setup.mock_get.return_value = mock_response

    input_url: str = "http://www.example.com"
    result: str = await interface.async_get_response_from_endpoint(input_url)

    assert_that(result).is_equal_to(expected)

    assert len(interface_test_setup.mock_get.call_args_list) == 1

    assert interface_test_setup.mock_get.call_args.args == (input_url,)

    assert len(interface_test_setup.mock_sleep.call_args_list) == 1
    assert interface_test_setup.mock_sleep.call_args.args == (3,)
