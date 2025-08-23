from pathlib import Path
from typing import Final
from pytest import MonkeyPatch
from configuration.app_config import AppConfig


FALLBACK_CONNECTION_STRING: Final[str] = "sqlite:///file::memory:?cache=shared&uri=true"


def test_app_config_defaults_when_no_files_and_no_env(monkeypatch: MonkeyPatch, tmp_path: Path) -> None:
    # No env var, no files
    monkeypatch.delenv("SIGHTSEEINGS_ENVIRONMENT", raising=False)
    monkeypatch.chdir(tmp_path)

    cfg = AppConfig()

    assert cfg.environment == "Development"
    assert cfg.connection_string == FALLBACK_CONNECTION_STRING


def test_app_config_reads_base_config_ini(monkeypatch: MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.delenv("SIGHTSEEINGS_ENVIRONMENT", raising=False)
    monkeypatch.chdir(tmp_path)

    (tmp_path / "config.ini").write_text(
        """
        [database]
        ConnectionString = sqlite:///base.db
        """.strip()
    )

    cfg = AppConfig()

    assert cfg.environment == "Development"
    assert cfg.connection_string == "sqlite:///base.db"


def test_app_config_environment_specific_overrides(monkeypatch: MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.setenv("SIGHTSEEINGS_ENVIRONMENT", "TestEnv")
    monkeypatch.chdir(tmp_path)

    # base config
    (tmp_path / "config.ini").write_text(
        """
        [database]
        ConnectionString = sqlite:///base.db
        """.strip()
    )

    # environment-specific override
    (tmp_path / "config.TestEnv.ini").write_text(
        """
        [database]
        ConnectionString = sqlite:///override.db
        """.strip()
    )

    cfg = AppConfig()

    assert cfg.environment == "TestEnv"
    assert cfg.connection_string == "sqlite:///override.db"
