import datetime
from app import db


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.Unicode(16), nullable=False)
    admin = db.Column(db.Boolean, default=False)
    password = db.Column(db.Unicode(256), nullable=True)

    user = db.relationship("Order", backref="user", lazy='dynamic')


class Order(db.Model):
    __tablename__ = "order"

    order_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    order_id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    address = db.Column(db.Unicode(128))
