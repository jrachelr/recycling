from flask import jsonify, request, url_for
from app import db
from app.models import Location, LocationSchema
from app.api import bp


@bp.route("/location/<int:id>", methods=["PUT", "GET", "DELETE"])
def get_location_by_id(id):
    location = Location.query.get_or_404(id)
    location_schema = LocationSchema()
    output = location_schema.dump(location)
    return jsonify({'Location': output})


@bp.route("/locations", methods=["GET"])
def get_locations():
    locations = Location.query.all()
    locations_schema = LocationSchema(many=True)
    output = locations_schema.dump(locations)
    return jsonify({'Locations': output})


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


@bp.route("/location/<int:id>/location_accepted_categories", methods=["PUT", "GET"])
def get_categories_by_location(id):
    cats = Location.query.get_or_404(id).location_accepted_categories
    return jsonify()
