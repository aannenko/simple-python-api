from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.base import Base
from models.sightseeing import Sightseeing


DEFAULT_CONNECTION_STRING = "sqlite:///sightseeings.db"

engine = create_engine(DEFAULT_CONNECTION_STRING, echo=True, future=True)
session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create() -> None:
    # Create DB
    Base.metadata.create_all(bind=engine)

    # Seed DB
    with session_factory() as session:
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
