from configparser import ConfigParser
from os import getenv


class AppConfig:
    def __init__(self) -> None:
        config = ConfigParser()
        config.read("config.ini")  # default config

        self.environment: str = getenv("SIGHTSEEINGS_ENVIRONMENT", "Development")
        config.read(f"config.{self.environment}.ini")  # environment-specific config

        self.connection_string: str = config.get(
            "database",  # section name
            "ConnectionString",  # option name
            fallback="sqlite:///file::memory:?cache=shared&uri=true",
        )

        self.create_database: bool = config.getboolean(
            "database", "CreateDatabase", fallback=True
        )

        self.seed_database: bool = config.getboolean(
            "database", "SeedDatabase", fallback=True
        )
