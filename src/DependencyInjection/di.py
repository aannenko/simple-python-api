import inject
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker

from Services.sightseeing_service import Session, SightseeingsService


def configure_inject(binder: inject.Binder) -> None:
    binder.bind(  # Singleton
        Engine, create_engine("sqlite:///sightseeings.db", echo=True, future=True)
    )
    binder.bind_to_constructor(  # Singleton
        sessionmaker[Session],
        lambda: sessionmaker(bind=inject.instance(Engine), expire_on_commit=False),
    )
    binder.bind_to_provider(  # Transient
        SightseeingsService,
        lambda: SightseeingsService(inject.instance(sessionmaker[Session])),
    )
