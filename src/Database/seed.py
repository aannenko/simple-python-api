from Database.db import SessionLocal
from Models.sightseeing import Sightseeing

def seed_db() -> None:
    with SessionLocal() as session:
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