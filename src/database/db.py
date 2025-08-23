import inject
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

from database.base import Base
from models.sightseeing import Sightseeing


DEFAULT_CONNECTION_STRING = "sqlite:///sightseeings.db"


def create_db_engine(connection_string: str = DEFAULT_CONNECTION_STRING) -> Engine:
    return create_engine(connection_string, echo=True, future=True)


def create_session_factory(engine: Engine) -> sessionmaker[Session]:
    return sessionmaker(bind=engine, expire_on_commit=False)


def create() -> None:
    # Create DB
    Base.metadata.create_all(bind=inject.instance(Engine))

    # Seed DB
    with inject.instance(sessionmaker[Session])() as session:
        if session.query(Sightseeing).count() == 0:
            session.add_all(
                [
                    Sightseeing("Statue of Liberty", "New York, NY"),
                    Sightseeing("Golden Gate Bridge", "San Francisco, CA"),
                    Sightseeing("Mount Rushmore", "Keystone, SD"),
                    Sightseeing("Grand Canyon", "Arizona"),
                    Sightseeing("Niagara Falls", "New York"),
                    Sightseeing("White House", "Washington, DC"),
                    Sightseeing("Disneyland", "Anaheim, CA"),
                    Sightseeing("Empire State Building", "New York, NY"),
                    Sightseeing("Times Square", "New York, NY"),
                    Sightseeing("Yosemite National Park", "California"),
                    Sightseeing("Las Vegas Strip", "Las Vegas, NV"),
                ]
            )
            session.commit()
