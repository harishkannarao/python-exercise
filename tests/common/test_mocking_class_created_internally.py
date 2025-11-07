from pathlib import Path
from unittest.mock import MagicMock

from pytest_mock import MockerFixture


def create_path(output_dir):
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    return


def test_path_mocking(mocker: MockerFixture):
    mock_mkdir: MagicMock = mocker.patch.object(
        Path, "mkdir", autospec=True, spec_set=True
    )

    create_path("/abc")

    assert len(mock_mkdir.call_args_list) == 1
    assert mock_mkdir.call_args_list[0].args == (Path("/abc"),)
    assert mock_mkdir.call_args_list[0].kwargs == {"parents": True, "exist_ok": True}
