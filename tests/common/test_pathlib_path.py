from dataclasses import dataclass
from pathlib import Path
from types import MappingProxyType

import pytest


def create_path(output_dir):
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    return


@dataclass(frozen=True)
class ArgsKwArgsPair:
    args: tuple
    kwargs: MappingProxyType


@dataclass(frozen=True)
class MkdirCall:
    path: str
    argsPair: ArgsKwArgsPair


@pytest.fixture
def path_mkdir_fixture(monkeypatch):
    mkdir_calls: list[MkdirCall] = []

    def mock_mkdir(self: Path, *args, **kwargs):
        mkdir_calls.append(
            MkdirCall(str(self), ArgsKwArgsPair(tuple(args), MappingProxyType(kwargs)))
        )
        return

    monkeypatch.setattr(Path, "mkdir", mock_mkdir)
    yield mkdir_calls


def test_path_mocking(path_mkdir_fixture: list[MkdirCall]):
    create_path("/abc")
    assert len(path_mkdir_fixture) == 1
    assert path_mkdir_fixture[0].path == "/abc"
    assert len(path_mkdir_fixture[0].argsPair.args) == 0
    assert path_mkdir_fixture[0].argsPair.kwargs.get("parents") is True
    assert path_mkdir_fixture[0].argsPair.kwargs.get("exist_ok") is True
