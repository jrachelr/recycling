from app import db

# TODO: complete Location model

# saved_locations = db.Table('saved_locations',
#                            db.Column('user_id', db.Integer, db.ForeignKey('User.id')),
#                            db.Column('location_id', db.Integer, db.ForeignKey('Location.id'))
#                            )


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    street_address = db.Column(db.String(40), nullable=False)
    city = db.Column(db.String(20), nullable=False)
    state = db.Column(db.String(20), nullable=False)

    # accepted_items = db.relationship('AcceptedItem', backref='')

    def __repr__(self) -> str:
        return f'Location({self.name}, {self.street_address}, {self.city}, {self.state})'


# class AcceptedItem(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
    # location_list =


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    # saved_locations = db.relationship('Location', secondary=saved_locations)
