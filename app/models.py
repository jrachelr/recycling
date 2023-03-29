from app import db
from flask import url_for


saved_locations = db.Table(
    "user_location",
    db.Column("user_id", db.Integer, db.ForeignKey("location.id")),
    db.Column("location_id", db.Integer, db.ForeignKey("user.id")),
)
accepted_categories = db.Table(
    "category_location",
    db.Column("category_id", db.Integer, db.ForeignKey("location.id")),
    db.Column("location_id", db.Integer, db.ForeignKey("category.id")),
)


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    street_address = db.Column(db.String(40), nullable=False)
    city = db.Column(db.String(20), nullable=False)

    # TODO: proper data type/ method of storage for all different values
    state = db.Column(db.String(20), nullable=False)

    def __repr__(self) -> str:
        return (
            f"Location({self.name}, {self.street_address}, {self.city}, {self.state})"
        )

    def to_dict(self):
        data = {
            "id": self.id,
            "name": self.name,
            "street_address": self.street_address,
            "city": self.city,
            "state": self.state,
        }
        return data

    def from_dict(self, data):
        for field in ["name", "street_address", "city", "state"]:
            if field in data:
                setattr(self, field, data[field])

    @staticmethod
    def to_collection_dict(query, endpoint, **kwargs):
        resources = query.paginate(error_out=False)
        data = {
            "items": [item.to_dict() for item in resources.items],
            "_meta": {
                # "page": page,
                # "per_page": per_page,
                "total_pages": resources.pages,
                "total_items": resources.total,
            },
            "_links": {
                "self": url_for(endpoint, **kwargs),
                "next": url_for(endpoint, **kwargs) if resources.has_next else None,
                "prev": url_for(endpoint, **kwargs) if resources.has_prev else None,
            },
        }
        return data


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    accepted_locations = db.relationship(
        "Location",
        secondary=accepted_categories,
        backref="location_accepted_categories",
    )

    # TODO: add material field with proper Column type
    # material = db.Column()

    def __repr__(self) -> str:
        return f"Category({self.name})"

    def to_dict(self):
        data = {"id": self.id, "name": self.name}
        return data

    def from_dict(self, data):
        for field in ["name"]:
            if field in data:
                setattr(self, field, data[field])

    @staticmethod
    def to_collection_dict(query, endpoint, **kwargs):
        resources = query.paginate(error_out=False)
        data = {
            "items": [item.to_dict() for item in resources.items],
            "_meta": {
                "total_pages": resources.pages,
                "total_items": resources.total,
            },
            "_links": {
                "self": url_for(endpoint, **kwargs),
                "next": url_for(endpoint, **kwargs) if resources.has_next else None,
                "prev": url_for(endpoint, **kwargs) if resources.has_prev else None,
            },
        }
        return data


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    saved_locations = db.relationship(
        "Location", secondary=saved_locations, backref="follower"
    )
