from unittest.mock import MagicMock

from assertpy import assert_that
from pytest_mock import MockerFixture

from app.service.process import get_response


def test_get_response_integration(mocker: MockerFixture) -> None:
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
    result: str = get_response(input_url)

    assert_that(result).is_equal_to(expected)

    assert len(mock_get_response_from_endpoint.call_args_list) == 1

    assert mock_get_response_from_endpoint.call_args.args == (input_url,)
