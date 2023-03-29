from flask import jsonify, request, url_for, abort
from app import db
from app.models import Location
from app.api import bp


@bp.route("/locations", methods=["GET"])
def get_locations():
    data = Location.to_collection_dict(Location.query, "api.get_locations")
    return jsonify(data)


@bp.route("/locations", methods=["POST"])
def create_location():
    data = request.get_json() or {}
    location = Location()
    location.from_dict(data)
    db.session.add(location)
    db.session.commit()
    response = jsonify(location.to_dict())
    response.status_code = 201
    # response.headers["Location"] = url_for("api.get_location", id=location.id)
    return response
