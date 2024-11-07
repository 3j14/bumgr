from pathlib import Path

import pytest
from bumgr import get_config
from tempfile import TemporaryDirectory
from pytest import MonkeyPatch
import os


# Note: Other config files, located e.g. at '/etc/bumgr/config.toml'
# or in the user path (if 'XDG_CONFIG_HOME' is not defined) are hard
# to test, because it requires accessing and changing the users files.


def test_get_config_xdg_config(monkeypatch: MonkeyPatch):
    with TemporaryDirectory() as temp_dir:
        config_dir = Path(temp_dir) / "bumgr"
        config_dir.mkdir(exist_ok=False)
        config_file = config_dir / "config.toml"
        config_file.touch(exist_ok=False)
        with monkeypatch.context() as m:
            m.setitem(os.environ, "XDG_CONFIG_HOME", temp_dir)
            config = get_config()
            assert config == config_file


def test_get_config_param():
    with TemporaryDirectory() as temp_dir:
        config_file = Path(temp_dir) / "config.toml"
        with pytest.raises(FileNotFoundError):
            get_config(str(config_file))
        config_file.touch(exist_ok=False)
        config = get_config(str(config_file))
        assert config == config_file
