import os

import pytest

from bumgr.backup import Backup
from bumgr.config import ConfigError


@pytest.fixture
def working_config():
    return {"source": "test", "repository": "test_repo", "password_file": "foo"}


@pytest.mark.parametrize("field", ["source", "repository", "password_file"])
def test_backup_check_config_required(
    field, working_config, monkeypatch: pytest.MonkeyPatch
):
    with monkeypatch.context() as m:
        m.delitem(os.environ, "RESTIC_REPOSITORY", raising=False)
        Backup.check_config(working_config)
        with pytest.raises(ConfigError):
            del working_config[field]
            Backup.check_config(working_config)
