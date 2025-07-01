from typing import List

from Database.db import SessionFactory
from Models.sightseeing import Sightseeing


class SightseeingsService:
    def get_sightseeings(self, skip: int, take: int) -> List[Sightseeing]:
        with SessionFactory() as session:
            return session.query(Sightseeing).offset(skip).limit(take).all()

    def get_sightseeing_by_id(self, id: int) -> Sightseeing:
        with SessionFactory() as session:
            sightseeing = session.query(Sightseeing).filter(Sightseeing.id == id).first()
            if sightseeing is None:
                raise IndexError("Sightseeing ID out of range")
            return sightseeing

    def add_sightseeing(self, sightseeing: Sightseeing) -> int:
        with SessionFactory() as session:
            session.add(sightseeing)
            session.commit()
            session.refresh(sightseeing)
            return sightseeing.id

    def try_update_sightseeing(self, id: int, sightseeing: Sightseeing) -> bool:
        with SessionFactory() as session:
            db_sightseeing = session.query(Sightseeing).filter(Sightseeing.id == id).first()
            if not db_sightseeing:
                return False
            db_sightseeing.name = sightseeing.name
            db_sightseeing.location = sightseeing.location
            session.commit()
            return True

    def try_delete_sightseeing(self, id: int) -> bool:
        with SessionFactory() as session:
            db_sightseeing = session.query(Sightseeing).filter(Sightseeing.id == id).first()
            if not db_sightseeing:
                return False
            session.delete(db_sightseeing)
            session.commit()
            return True
