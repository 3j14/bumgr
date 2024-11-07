from pathlib import Path
from bumgr import get_config
from tempfile import TemporaryDirectory
from pytest import MonkeyPatch
import os


def test_get_config(monkeypatch: MonkeyPatch):
    with TemporaryDirectory() as temp_dir:
        config_dir = Path(temp_dir) / "bumgr"
        config_dir.mkdir(exist_ok=False)
        config_file = config_dir / "config.toml"
        config_file.touch(exist_ok=False)
        with monkeypatch.context() as m:
            m.setitem(os.environ, "XDG_CONFIG_HOME", temp_dir)
            config = get_config()
            assert config == config_file
