from configparser import ConfigParser


class AppConfig:
    def __init__(self) -> None:
        config = ConfigParser()
        config.read("config.ini")

        self.connection_string: str = config.get(
            "database",  # section name
            "ConnectionString",  # option name
            fallback="sqlite:///file::memory:?cache=shared&uri=true",
        )
