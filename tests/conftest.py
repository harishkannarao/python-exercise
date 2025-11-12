from dataclasses import dataclass
from unittest.mock import MagicMock, AsyncMock

import pytest
from pytest_mock import MockerFixture


@dataclass(frozen=True)
class InterfaceSetup:
    mock_get: MagicMock
    mock_sleep: AsyncMock


@pytest.fixture
def interface_test_setup(mocker: MockerFixture) -> InterfaceSetup:
    mock_get: MagicMock = mocker.patch("app.external.interface.requests.get")
    mock_sleep: AsyncMock = mocker.patch("app.external.interface.asyncio.sleep")
    return InterfaceSetup(mock_get=mock_get, mock_sleep=mock_sleep)
