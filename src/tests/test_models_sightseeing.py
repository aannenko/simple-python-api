from models.sightseeing import Sightseeing


def test_sightseeing_to_dict_includes_fields_and_id_default_none() -> None:
    s = Sightseeing(name="Eiffel Tower", location="Paris")
    d = s.to_dict()
    # id is not set until persisted; SQLAlchemy will default to None on transient instances
    assert set(d.keys()) == {"id", "name", "location"}
    assert d["id"] is None
    assert d["name"] == "Eiffel Tower"
    assert d["location"] == "Paris"
