import inject
from sqlalchemy import Engine
from sqlalchemy.orm import Session, sessionmaker

from configuration.app_config import AppConfig
from database.db import create_db_engine, create_session_factory
from services.sightseeing_service import SightseeingService


def configure_inject(binder: inject.Binder) -> None:
    binder.bind(AppConfig, AppConfig())  # Singleton
    binder.bind_to_constructor(  # Singleton
        Engine,
        lambda: create_db_engine(inject.instance(AppConfig).connection_string),
    )
    binder.bind_to_constructor(  # Singleton
        sessionmaker[Session],
        lambda: create_session_factory(inject.instance(Engine)),
    )
    binder.bind_to_provider(  # Transient
        SightseeingService,
        lambda: SightseeingService(inject.instance(sessionmaker[Session])),
    )
