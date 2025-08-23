import inject
from sqlalchemy import Engine
from sqlalchemy.orm import Session, sessionmaker

from database.db import create_db_engine, create_session_factory
from services.sightseeing_service import SightseeingService


def configure_inject(binder: inject.Binder) -> None:
    binder.bind(Engine, create_db_engine())  # Singleton
    binder.bind_to_constructor(  # Singleton
        sessionmaker[Session],
        lambda: create_session_factory(inject.instance(Engine)),
    )
    binder.bind_to_provider(  # Transient
        SightseeingService,
        lambda: SightseeingService(inject.instance(sessionmaker[Session])),
    )
