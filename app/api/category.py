from flask import jsonify, request
from app import db
from app.models import Category, CategorySchema
from app.api import bp


@bp.route("/category/<int:id>", methods=["PUT", "GET", "DELETE"])
def get_category_by_id(id):
    category = Category.query.get_or_404(id)
    category_schema = CategorySchema()
    output = category_schema.dump(category)
    return jsonify({'Category': output})


@bp.route("/categories", methods=["GET"])
def get_categories():
    categories = Category.query.all()
    categories_schema = CategorySchema(many=True)
    output = categories_schema.dump(categories)
    return jsonify({'Categories': output})


@bp.route("/new_category", methods=["POST"])
def create_category():
    # TODO: add link to self in response
    # TODO: add data validation
    json_data = request.get_json()
    category_schema = CategorySchema()

    if not json_data:
        return {'message': 'No input data provided'}, 400
    data = category_schema.load(json_data)

    """ Validate data and deserialize input
    try:
        data = category_schema.load(json_data)
    except ValidationError as err:
        return err.messages, 422
    """
    category = Category(name=data['name'])
    db.session.add(category)
    db.session.commit()

    result = category_schema.dump(Category.query.get(category.id))
    return {'message': 'Created new category', 'category': result}


@bp.route("/categories/<int:id>/locations")
def get_locations_by_category(id):
    category = Category.query.get_or_404(id)
    locations = category.accepted_locations

    location_list = []

    for loc in locations:
        location_list.append(loc.to_dict())

    location_dict = {"items": location_list}
    return jsonify(location_dict)
