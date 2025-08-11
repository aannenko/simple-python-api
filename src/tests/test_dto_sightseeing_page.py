from dto.sightseeing_page import SightseeingPage
from models.sightseeing import Sightseeing


def test_sightseeing_page_to_dict_maps_items_and_pagination_fields() -> None:
    items = [Sightseeing("A", "X"), Sightseeing("B", "Y")]
    page = SightseeingPage(items, previous_page="/prev", next_page="/next")

    d = page.to_dict()

    assert d["previous_page"] == "/prev"
    assert d["next_page"] == "/next"
    assert isinstance(d["sightseeings"], list)
    assert len(d["sightseeings"]) == 2
    assert d["sightseeings"][0]["name"] == "A"
    assert d["sightseeings"][0]["location"] == "X"
