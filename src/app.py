from flask import Flask, jsonify, request

from Models.sightseeing import Sightseeing
from DTO.sightseeing_page import SightseeingPage
from Services.sightseeing_service import SightseeingsService

app = Flask(__name__)

sightseeings_service = SightseeingsService()


@app.get("/sightseeings")
def get_sightseeings():
    skip = request.args.get("skip", default=0, type=int)
    take = request.args.get("take", default=10, type=int)
    if skip < 0:
        return jsonify({"error": "skip must be non-negative"}), 400
    if take <= 0 or take > 100:
        return jsonify({"error": "take must be between 1 and 100"}), 400

    sightseeings = sightseeings_service.get_sightseeings(skip, take)
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

    result = page.__dict__.copy()
    result["sightseeings"] = [s.__dict__ for s in page.sightseeings]
    return jsonify(result)


@app.get("/sightseeings/<int:id>")
def get_sightseeing_by_id(id: int):
    try:
        return jsonify(sightseeings_service.get_sightseeing_by_id(id).__dict__)
    except IndexError:
        return jsonify({"error": "Sightseeing not found"}), 404


@app.post("/sightseeings")
def add_sightseeing():
    data = request.json
    if not data or "name" not in data or "location" not in data:
        return jsonify({"error": "Invalid data"}), 400

    sightseeing = Sightseeing(data["name"], data["location"])
    id = sightseeings_service.add_sightseeing(sightseeing)

    return "", 201, {"Location": f"/sightseeings/{id}"}


@app.patch("/sightseeings/<int:id>")
def update_sightseeing(id: int):
    data = request.json
    if not data or "name" not in data or "location" not in data:
        return jsonify({"error": "Invalid data"}), 400

    sightseeing = Sightseeing(data["name"], data["location"])
    if sightseeings_service.try_update_sightseeing(id, sightseeing):
        return "", 204
    else:
        return jsonify({"error": "Sightseeing not found"}), 404


@app.delete("/sightseeings/<int:id>")
def delete_sightseeing(id: int):
    if sightseeings_service.try_delete_sightseeing(id):
        return "", 204
    else:
        return jsonify({"error": "Sightseeing not found"}), 404
