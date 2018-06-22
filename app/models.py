from app import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True,)
    phone = db.Column(db.Text)
    address = db.Column(db.Text)
    admin = db.Column(db.Boolean, unique=False, default=False)
    password = db.Column(db.Text)
