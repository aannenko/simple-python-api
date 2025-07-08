from configparser import ConfigParser
from os import getenv, path


class AppConfig:
    def __init__(self) -> None:
        config = ConfigParser()
        config.read("config.ini")  # default config values

        self.environment: str = getenv("SIGHTSEEINGS_ENVIRONMENT", "Development")
        env_config_path = path.join("environment", f"config.{self.environment}.ini")
        config.read(env_config_path)  # environment-specific config values

        self.connection_string: str = config.get(
            "database",  # section name
            "ConnectionString",  # option name
            fallback="sqlite:///file::memory:?cache=shared&uri=true",
        )
