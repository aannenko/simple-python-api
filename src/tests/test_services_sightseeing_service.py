from __future__ import annotations

from typing import Iterator

import pytest
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

from database.base import Base
from models.sightseeing import Sightseeing
from services.sightseeing_service import SightseeingService


@pytest.fixture()
def session_factory() -> Iterator[sessionmaker[Session]]:
    # Use a shared in-memory SQLite database per Engine via StaticPool
    engine: Engine = create_engine(
        "sqlite:///:memory:",
        echo=False,
        future=True,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(bind=engine)

    factory: sessionmaker[Session] = sessionmaker(bind=engine, expire_on_commit=False)
    try:
        yield factory
    finally:
        engine.dispose()


@pytest.fixture()
def service(session_factory: sessionmaker[Session]) -> SightseeingService:
    return SightseeingService(session_factory)


# Helpers

def seed(session_factory: sessionmaker[Session]) -> list[Sightseeing]:
    with session_factory() as session:
        items = [
            Sightseeing("A", "X"),
            Sightseeing("B", "Y"),
            Sightseeing("C", "Z"),
        ]
        session.add_all(items)
        session.commit()
        # refresh to get IDs
        for item in items:
            session.refresh(item)
        return items


# Tests

def test_get_sightseeings_pagination(
    service: SightseeingService, session_factory: sessionmaker[Session]
) -> None:
    items = seed(session_factory)

    page1 = service.get_sightseeings(skip=0, take=2)
    assert len(page1) == 2
    assert {s.name for s in page1} <= {"A", "B", "C"}

    page2 = service.get_sightseeings(skip=2, take=2)
    assert len(page2) == 1
    assert {s.name for s in page2} == {items[2].name}


def test_get_sightseeing_by_id_found_and_not_found(
    service: SightseeingService, session_factory: sessionmaker[Session]
) -> None:
    items = seed(session_factory)
    found = service.get_sightseeing_by_id(items[0].id)
    assert found.name == items[0].name

    with pytest.raises(IndexError):
        service.get_sightseeing_by_id(9999)


def test_add_sightseeing_persists_and_returns_id(
    service: SightseeingService, session_factory: sessionmaker[Session]
) -> None:
    new_id = service.add_sightseeing(Sightseeing("D", "W"))
    assert isinstance(new_id, int)

    # verify persisted
    with session_factory() as session:
        row = session.query(Sightseeing).filter(Sightseeing.id == new_id).first()
        assert row is not None
        assert row.name == "D"
        assert row.location == "W"


def test_try_update_sightseeing_returns_true_when_updated(
    service: SightseeingService, session_factory: sessionmaker[Session]
) -> None:
    items = seed(session_factory)
    ok = service.try_update_sightseeing(items[0].id, Sightseeing("A2", "X2"))
    assert ok is True

    with session_factory() as session:
        row = session.get(Sightseeing, items[0].id)
        assert row is not None
        assert row.name == "A2"
        assert row.location == "X2"


def test_try_update_sightseeing_returns_false_when_missing(
    service: SightseeingService,
) -> None:
    ok = service.try_update_sightseeing(12345, Sightseeing("NA", "NA"))
    assert ok is False


def test_try_delete_sightseeing_returns_true_and_removes(
    service: SightseeingService, session_factory: sessionmaker[Session]
) -> None:
    items = seed(session_factory)
    ok = service.try_delete_sightseeing(items[1].id)
    assert ok is True

    with pytest.raises(IndexError):
        service.get_sightseeing_by_id(items[1].id)


def test_try_delete_sightseeing_returns_false_when_missing(
    service: SightseeingService,
) -> None:
    ok = service.try_delete_sightseeing(54321)
    assert ok is False
