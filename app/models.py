from app import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True,)
    phone = db.Column(db.Unicode(16))
    address = db.Column(db.Unicode(128))
    admin = db.Column(db.Boolean, default=False)
    password = db.Column(db.Unicode(256))
