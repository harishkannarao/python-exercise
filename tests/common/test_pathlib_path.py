from pathlib import Path

from pytest_mock import MockerFixture


def create_path(output_dir):
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    return


def test_path_mocking(mocker: MockerFixture):
    instances: list[str] = []
    args_list: list[tuple] = []
    kwargs_list: list[dict] = []

    def mock_mkdir(self: Path, *args, **kwargs):
        instances.append(str(self))
        args_list.append(args)
        kwargs_list.append(kwargs)
        return

    mocker.patch.object(Path, "mkdir", mock_mkdir)

    create_path("/abc")
    assert len(instances) == 1
    assert len(args_list) == 1
    assert len(kwargs_list) == 1
    assert instances[0] == "/abc"
    assert args_list[0] == ()
    assert kwargs_list[0] == {"parents": True, "exist_ok": True}
