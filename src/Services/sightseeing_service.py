from sqlalchemy.orm import Session, sessionmaker
from typing import List

from Models.sightseeing import Sightseeing


class SightseeingsService:
    def __init__(self, session_factory: sessionmaker[Session]) -> None:
        self.session_factory = session_factory

    def get_sightseeings(self, skip: int, take: int) -> List[Sightseeing]:
        with self.session_factory() as session:
            return session.query(Sightseeing).offset(skip).limit(take).all()

    def get_sightseeing_by_id(self, id: int) -> Sightseeing:
        with self.session_factory() as session:
            sightseeing = session.query(Sightseeing).filter(Sightseeing.id == id).first()
            if sightseeing is None:
                raise IndexError("Sightseeing ID out of range")
            return sightseeing

    def add_sightseeing(self, sightseeing: Sightseeing) -> int:
        with self.session_factory() as session:
            session.add(sightseeing)
            session.commit()
            session.refresh(sightseeing)
            return sightseeing.id

    def try_update_sightseeing(self, id: int, sightseeing: Sightseeing) -> bool:
        with self.session_factory() as session:
            db_sightseeing = session.query(Sightseeing).filter(Sightseeing.id == id).first()
            if not db_sightseeing:
                return False
            db_sightseeing.name = sightseeing.name
            db_sightseeing.location = sightseeing.location
            session.commit()
            return True

    def try_delete_sightseeing(self, id: int) -> bool:
        with self.session_factory() as session:
            db_sightseeing = session.query(Sightseeing).filter(Sightseeing.id == id).first()
            if not db_sightseeing:
                return False
            session.delete(db_sightseeing)
            session.commit()
            return True
