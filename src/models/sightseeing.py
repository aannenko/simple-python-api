from sqlalchemy.orm import Mapped, mapped_column

from database.base import Base


class Sightseeing(Base):
    __tablename__ = "sightseeings"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    location: Mapped[str]

    def __init__(self, name: str, location: str) -> None:
        self.name = name
        self.location = location

    def to_dict(self) -> dict[str, int | str]:
        return {"id": self.id, "name": self.name, "location": self.location}
