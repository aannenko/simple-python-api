from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.base import Base
from models.sightseeing import Sightseeing

DATABASE_URL = "sqlite:///sightseeings.db"

engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create() -> None:
    Base.metadata.create_all(bind=engine)

def seed() -> None:
    with SessionFactory() as session:
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
