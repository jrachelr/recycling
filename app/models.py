from app import db


saved_locations = db.Table('saved_locations',
                           db.Column('user_id', db.Integer,
                                     db.ForeignKey('location.id')),
                           db.Column('location_id', db.Integer,
                                     db.ForeignKey('user.id'))
                           )


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    street_address = db.Column(db.String(40), nullable=False)
    city = db.Column(db.String(20), nullable=False)

    # TODO: proper data type/ method of storage for all different values
    state = db.Column(db.String(20), nullable=False)

    def __repr__(self) -> str:
        return f'Location({self.name}, {self.street_address}, {self.city}, {self.state})'


class AcceptedItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_type = db.Column(db.String(20), nullable=False)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    saved_locations = db.relationship(
        'Location', secondary=saved_locations, backref='saved_locations')
