from unittest.mock import MagicMock

from pytest import MonkeyPatch
from pytest_mock import MockerFixture


class Test:
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b


def test_add_real() -> None:
    result: int = Test.add(2, 2)
    assert result == 4


def test_add_mocked_with_monkey_patch(monkeypatch: MonkeyPatch) -> None:
    mock_add: MagicMock = MagicMock()
    mock_add.side_effect = [3, 5]
    monkeypatch.setattr(Test, "add", mock_add)

    assert Test.add(2, 3) == 3
    assert Test.add(a=3, b=4) == 5

    calls_made: list = mock_add.call_args_list
    assert len(calls_made) == 2
    assert calls_made[0].args[0] == 2
    assert calls_made[0].args[1] == 3
    assert calls_made[1].kwargs["a"] == 3
    assert calls_made[1].kwargs["b"] == 4


def test_add_mocked_with_mocker(mocker: MockerFixture) -> None:
    mock_add: MagicMock = MagicMock()
    mock_add.side_effect = [3, 5]
    mocker.patch.object(Test, "add", mock_add)

    assert Test.add(2, 3) == 3
    assert Test.add(a=3, b=4) == 5

    calls_made: list = mock_add.call_args_list
    assert len(calls_made) == 2
    assert calls_made[0].args[0] == 2
    assert calls_made[0].args[1] == 3
    assert calls_made[1].kwargs["a"] == 3
    assert calls_made[1].kwargs["b"] == 4
