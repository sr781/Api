from app.database import db


class Address(db.Model):
    """Model to represent an Address record in DB."""
    __tablename__ = "address"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    street = db.Column(db.String(200), nullable=True)
    suite = db.Column(db.String(125), nullable=True)
    city = db.Column(db.String(80), nullable=True)
    zipcode = db.Column(db.String(20), nullable=True)
    lat = db.Column(db.String(20), nullable=True)
    long = db.Column(db.String(20), nullable=True)
    user = db.relationship("User", back_populates="addresses")

    def __init__(self, user_id, street, suite, city,
                 zipcode, lat, long):
        self.user_id = user_id
        self.street = street
        self.suite = suite
        self.city = city
        self.zipcode = zipcode
        self.lat = lat
        self.long = long


