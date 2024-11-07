import pytest

from bumgr.backup import Backup
from bumgr.config import ConfigError


@pytest.fixture
def working_config():
    return {"source": "test", "repository": "test_repo", "password_file": "foo"}


@pytest.fixture
def clean_env():
    mpatch = pytest.MonkeyPatch()
    with mpatch.context() as m:
        m.delenv("RESTIC_REPOSITORY", raising=False)
        m.delenv("RESTIC_PASSWORD_FILE", raising=False)
        m.delenv("RESTIC_PASSWORD_COMMAND", raising=False)
        yield


@pytest.mark.parametrize("field", ["source", "repository", "password_file"])
def test_backup_check_config_required(field, working_config, clean_env):
    Backup.check_config(working_config)
    with pytest.raises(ConfigError):
        del working_config[field]
        Backup.check_config(working_config)


def test_backup_check_config_password_exclusive(working_config, clean_env):
    Backup.check_config(working_config)
    with pytest.raises(ConfigError):
        working_config["password_command"] = "should not be set"
        Backup.check_config(working_config)
