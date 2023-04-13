from app import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


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


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    saved_locations = db.relationship(
        "Location", secondary=saved_locations, backref="follower"
    )


class LocationSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Location


class CategorySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Category
