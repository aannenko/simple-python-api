from typing import Literal
from flask import Flask, Response, jsonify, request

from dto.sightseeing_page import SightseeingPage
from models.sightseeing import Sightseeing
from services.sightseeing_service import SightseeingService


sightseeing_service = SightseeingService()


def register(app: Flask) -> None:
    app.get("/sightseeings")(get_sightseeings)
    app.get("/sightseeings/<int:id>")(get_sightseeing_by_id)
    app.post("/sightseeings")(add_sightseeing)
    app.patch("/sightseeings/<int:id>")(update_sightseeing)
    app.delete("/sightseeings/<int:id>")(delete_sightseeing)


def get_sightseeings() -> tuple[Response, Literal[400]] | Response:
    skip = request.args.get("skip", default=0, type=int)
    take = request.args.get("take", default=10, type=int)
    if skip < 0:
        return jsonify({"error": "skip must be non-negative"}), 400
    if take <= 0 or take > 100:
        return jsonify({"error": "take must be between 1 and 100"}), 400

    sightseeings = sightseeing_service.get_sightseeings(skip, take)
    page = SightseeingPage(
        sightseeings,
        (
            ""
            if skip == 0
            else "/sightseeings?skip={}&take={}".format(max(skip - take, 0), take)
        ),
        (
            ""
            if len(sightseeings) < take
            else "/sightseeings?skip={}&take={}".format(skip + take, take)
        ),
    )

    return jsonify(page.to_dict())


def get_sightseeing_by_id(id: int) -> Response | tuple[Response, Literal[404]]:
    try:
        return jsonify(sightseeing_service.get_sightseeing_by_id(id).to_dict())
    except IndexError:
        return jsonify({"error": "Sightseeing not found"}), 404


def add_sightseeing() -> tuple[Response, Literal[400]] | tuple[Literal[''], Literal[201], dict[str, str]]:
    data = request.json
    if not data or "name" not in data or "location" not in data:
        return jsonify({"error": "Invalid data"}), 400

    sightseeing = Sightseeing(data["name"], data["location"])
    id = sightseeing_service.add_sightseeing(sightseeing)

    return "", 201, {"Location": f"/sightseeings/{id}"}


def update_sightseeing(id: int) -> tuple[Response, Literal[400]] | tuple[Literal[''], Literal[204]] | tuple[Response, Literal[404]]:
    data = request.json
    if not data or "name" not in data or "location" not in data:
        return jsonify({"error": "Invalid data"}), 400

    sightseeing = Sightseeing(data["name"], data["location"])
    if sightseeing_service.try_update_sightseeing(id, sightseeing):
        return "", 204
    else:
        return jsonify({"error": "Sightseeing not found"}), 404


def delete_sightseeing(id: int) -> tuple[Literal[''], Literal[204]] | tuple[Response, Literal[404]]:
    if sightseeing_service.try_delete_sightseeing(id):
        return "", 204
    else:
        return jsonify({"error": "Sightseeing not found"}), 404
