from unittest.mock import MagicMock
from pytest import MonkeyPatch
from assertpy import assert_that
from pytest_mock import MockerFixture
import app.service.process
import app.external.interface
from app.service.process import get_response


def test_get_response_using_monkey_patch(monkeypatch: MonkeyPatch) -> None:
    mock_get_response_from_endpoint: MagicMock = MagicMock()
    monkeypatch.setattr(
        app.service.process,
        "get_response_from_endpoint",
        mock_get_response_from_endpoint,
    )

    expected: str = "test-response"
    mock_get_response_from_endpoint.return_value = expected

    input_url: str = "http://www.example.com"
    result: str = get_response(input_url)

    assert_that(result).is_equal_to(expected)

    assert len(mock_get_response_from_endpoint.call_args_list) == 1

    assert mock_get_response_from_endpoint.call_args.args == (input_url,)


def test_get_response_mocker_fixture(mocker: MockerFixture) -> None:
    mock_get_response_from_endpoint: MagicMock = MagicMock()
    mocker.patch(
        "app.service.process.get_response_from_endpoint",
        mock_get_response_from_endpoint,
    )

    expected: str = "test-response"
    mock_get_response_from_endpoint.return_value = expected

    input_url: str = "http://www.example.com"
    result: str = get_response(input_url)

    assert_that(result).is_equal_to(expected)

    assert len(mock_get_response_from_endpoint.call_args_list) == 1

    assert mock_get_response_from_endpoint.call_args.args == (input_url,)


def test_get_response_integration_with_mocker(mocker: MockerFixture) -> None:
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
