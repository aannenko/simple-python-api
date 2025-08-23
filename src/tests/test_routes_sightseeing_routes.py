from typing import Iterator

import pytest
from flask.testing import FlaskClient


@pytest.fixture()
def client(monkeypatch: pytest.MonkeyPatch) -> Iterator[FlaskClient]:
    monkeypatch.setenv("SIGHTSEEINGS_ENVIRONMENT", "Testing")

    import app as app_module

    app = app_module.app
    with app.test_client() as c:
        yield c


# Helpers

def create_sightseeing(client: FlaskClient, name: str, location: str) -> int:
    res = client.post("/sightseeings", json={"name": name, "location": location})
    assert res.status_code == 201
    loc = res.headers.get("Location")
    assert loc and loc.startswith("/sightseeings/")
    return int(loc.rsplit("/", 1)[1])


# Tests

def test_get_sightseeings_empty(client: FlaskClient) -> None:
    res = client.get("/sightseeings")
    assert res.status_code == 200
    data = res.get_json()
    assert data["sightseeings"] == []
    assert data["previous_page"] == ""
    assert data["next_page"] == ""


def test_post_invalid_payload(client: FlaskClient) -> None:
    # missing fields
    res = client.post("/sightseeings", json={"name": "OnlyName"})
    assert res.status_code == 400

    # no json
    res = client.post("/sightseeings")
    # Flask 3 returns 415 Unsupported Media Type when no JSON is provided
    assert res.status_code == 415


def test_crud_happy_path(client: FlaskClient) -> None:
    new_id = create_sightseeing(client, "A", "X")

    # GET by id
    res = client.get(f"/sightseeings/{new_id}")
    assert res.status_code == 200
    data = res.get_json()
    assert data["id"] == new_id
    assert data["name"] == "A"
    assert data["location"] == "X"

    # PATCH
    res = client.patch(f"/sightseeings/{new_id}", json={"name": "A2", "location": "X2"})
    assert res.status_code == 204

    # Verify update
    res = client.get(f"/sightseeings/{new_id}")
    assert res.status_code == 200
    data = res.get_json()
    assert data["name"] == "A2"
    assert data["location"] == "X2"

    # DELETE
    res = client.delete(f"/sightseeings/{new_id}")
    assert res.status_code == 204

    # Verify 404 after delete
    res = client.get(f"/sightseeings/{new_id}")
    assert res.status_code == 404


def test_pagination_links_and_bounds(client: FlaskClient) -> None:
    for i in range(3):
        create_sightseeing(client, f"S{i}", f"L{i}")

    # First page
    res = client.get("/sightseeings?skip=0&take=2")
    assert res.status_code == 200
    data = res.get_json()
    assert len(data["sightseeings"]) == 2
    assert data["previous_page"] == ""
    assert data["next_page"].startswith("/sightseeings?skip=2&take=2")

    # Second page
    res = client.get("/sightseeings?skip=2&take=2")
    assert res.status_code == 200
    data = res.get_json()
    assert len(data["sightseeings"]) == 1
    assert data["next_page"] == ""
    assert data["previous_page"].startswith("/sightseeings?skip=0&take=2")

    # Validation
    assert client.get("/sightseeings?skip=-1").status_code == 400
    assert client.get("/sightseeings?take=0").status_code == 400
    assert client.get("/sightseeings?take=101").status_code == 400


def test_update_and_delete_not_found_and_invalid(client: FlaskClient) -> None:
    # Not found
    assert client.patch("/sightseeings/999", json={"name": "N", "location": "L"}).status_code == 404
    assert client.delete("/sightseeings/999").status_code == 404

    # Invalid body
    sid = create_sightseeing(client, "B", "Y")
    assert client.patch(f"/sightseeings/{sid}", json={"name": "OnlyName"}).status_code == 400
