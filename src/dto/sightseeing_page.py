from models.sightseeing import Sightseeing


class SightseeingPage:
    def __init__(
        self,
        sightseeings: list[Sightseeing],
        previous_page: str = "",
        next_page: str = "",
    ) -> None:
        self.sightseeings = sightseeings
        self.previous_page = previous_page
        self.next_page = next_page

    def to_dict(self) -> dict[str, list[dict[str, int | str]] | str]:
        return {
            "sightseeings": [s.to_dict() for s in self.sightseeings],
            "previous_page": self.previous_page,
            "next_page": self.next_page,
        }
