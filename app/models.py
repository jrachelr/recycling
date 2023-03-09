from app import db

# TODO: complete Location model


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f'Location(name={self.name}, address={self.address})'

# TODO:
# class User(db.Model):
