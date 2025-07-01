import inject
from sqlalchemy.orm import Session, sessionmaker

from DependencyInjection.di import Engine
from Models.sightseeing import Base, Sightseeing


def create() -> None:
    Base.metadata.create_all(bind=inject.instance(Engine))


def seed() -> None:
    session_factory = inject.instance(sessionmaker[Session])
    with session_factory() as session:
        if session.query(Sightseeing).count() == 0:
            session.add_all([
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
            ])
            session.commit()
