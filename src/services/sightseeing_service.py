from sqlalchemy import insert
from sqlalchemy.orm import Session, sessionmaker
from typing import List

from models.sightseeing import Sightseeing


class SightseeingService:
    def __init__(self, session_factory: sessionmaker[Session]) -> None:
        self.session_factory = session_factory

    def get_sightseeings(self, skip: int, take: int) -> List[Sightseeing]:
        with self.session_factory() as session:
            return session.query(Sightseeing).offset(skip).limit(take).all()

    def get_sightseeing_by_id(self, id: int) -> Sightseeing:
        with self.session_factory() as session:
            db_sightseeing = (
                session.query(Sightseeing).filter(Sightseeing.id == id).first()
            )
            if db_sightseeing is None:
                raise IndexError("Sightseeing ID out of range")
            return db_sightseeing

    def add_sightseeing(self, sightseeing: Sightseeing) -> int:
        with self.session_factory() as session:
            statement = (
                insert(Sightseeing)
                .values(name=sightseeing.name, location=sightseeing.location)
                .returning(Sightseeing.id)
            )
            inserted_id = session.execute(statement).scalar_one()
            session.commit()
            return inserted_id

    def try_update_sightseeing(self, id: int, sightseeing: Sightseeing) -> bool:
        with self.session_factory() as session:
            rows_updated = (
                session.query(Sightseeing)
                .filter(Sightseeing.id == id)
                .update(
                    {
                        Sightseeing.name: sightseeing.name,
                        Sightseeing.location: sightseeing.location,
                    },
                    synchronize_session=False,
                )
            )
            session.commit()
            return rows_updated > 0

    def try_delete_sightseeing(self, id: int) -> bool:
        with self.session_factory() as session:
            rows_deleted = (
                session.query(Sightseeing)
                .filter(Sightseeing.id == id)
                .delete(synchronize_session=False)
            )
            session.commit()
            return rows_deleted > 0
