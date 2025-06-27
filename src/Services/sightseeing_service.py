from Models.sightseeing import Sightseeing
from Database.db import SessionLocal
from typing import List


class SightseeingsService:
    def get_sightseeings(self, skip: int, take: int) -> List[Sightseeing]:
        with SessionLocal() as session:
            return session.query(Sightseeing).offset(skip).limit(take).all()

    def get_sightseeing_by_id(self, id: int) -> Sightseeing:
        with SessionLocal() as session:
            sightseeing = session.query(Sightseeing).filter(Sightseeing.id == id).first()
            if sightseeing is None:
                raise IndexError("Sightseeing ID out of range")
            return sightseeing

    def add_sightseeing(self, sightseeing: Sightseeing) -> int:
        with SessionLocal() as session:
            session.add(sightseeing)
            session.commit()
            session.refresh(sightseeing)
            return sightseeing.id

    def try_update_sightseeing(self, id: int, sightseeing: Sightseeing) -> bool:
        with SessionLocal() as session:
            db_sightseeing = session.query(Sightseeing).filter(Sightseeing.id == id).first()
            if not db_sightseeing:
                return False
            db_sightseeing.name = sightseeing.name
            db_sightseeing.location = sightseeing.location
            session.commit()
            return True

    def try_delete_sightseeing(self, id: int) -> bool:
        with SessionLocal() as session:
            db_sightseeing = session.query(Sightseeing).filter(Sightseeing.id == id).first()
            if not db_sightseeing:
                return False
            session.delete(db_sightseeing)
            session.commit()
            return True
