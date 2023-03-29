from flask import jsonify, request, url_for
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
    response.headers["Location"] = url_for(
        "api.get_location_by_id", location_id=location.id
    )
    return response


@bp.route("/location/<int:location_id>", methods=["PUT", "GET", "DELETE"])
def get_location_by_id(location_id):
    return jsonify(Location.query.get_or_404(location_id).to_dict())


# TODO:
# - get location by item ID
