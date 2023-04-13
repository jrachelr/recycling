from flask import jsonify, request
from app import db
from app.models import Location, LocationSchema, CategorySchema
from app.api import bp
# from marshmallow import ValidationError


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


@bp.route("/new_location", methods=["POST"])
def create_location():
    # TODO: add data validation
    json_data = request.get_json()
    location_schema = LocationSchema()

    if not json_data:
        return {'message': 'No input data provided'}, 400
    data = location_schema.load(json_data)

    """ Validate data and deserialize input
    try:
        data = location_schema.load(json_data)
    except ValidationError as err:
        return err.messages, 422
    """
    location = Location(
        name=data['name'], street_address=data['street_address'], city=data['city'], state=data['state'])
    db.session.add(location)
    db.session.commit()

    result = location_schema.dump(Location.query.get(location.id))
    return {'message': 'Created new location', 'location': result}


@bp.route("/location/<int:id>/categories", methods=["PUT", "GET"])
def get_categories_by_location(id):
    location = Location.query.get_or_404(id)
    categories = location.location_accepted_categories
    category_schema = CategorySchema(many=True)
    output = category_schema.dump(categories)

    return jsonify(
        {
            'Location': location.name,
            'Accepted categories': output
        })
