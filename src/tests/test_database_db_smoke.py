from pathlib import Path

from sqlalchemy.orm import Session, sessionmaker

from database.base import Base
from database.db import create_db_engine, create_session_factory
from models.sightseeing import Sightseeing


def test_metadata_create_all_with_helper_engine(tmp_path: Path) -> None:
    db_path = tmp_path / "smoke.db"
    engine = create_db_engine(f"sqlite:///{db_path}")

    # Should not raise
    Base.metadata.create_all(bind=engine)

    factory: sessionmaker[Session] = create_session_factory(engine)
    with factory() as session:
        # Simple smoke query against a created table
        count = session.query(Sightseeing).count()
        assert count == 0
