from flask import jsonify, request, url_for
from app import db
from app.models import Category
from app.api import bp


@bp.route("/categories", methods=["POST"])
def create_category():
    data = request.get_json() or {}
    category = Category()
    category.from_dict(data)
    db.session.add(category)
    db.session.commit()
    response = jsonify(category.to_dict())
    response.status_code = 201
    # response.headers["Category"] = url_for(
    #     "api.get_location_by_id", location_id=location.id
    # )
    return response


@bp.route("/categories/<int:id>/locations")
def get_locations_by_category(id):
    category = Category.query.get_or_404(id)
    locations = category.accepted_locations

    location_list = []

    for loc in locations:
        location_list.append(loc.to_dict())

    location_dict = {"items": location_list}
    return jsonify(location_dict)
