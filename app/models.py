from app import db
from sqlalchemy.orm import backref


# class Users(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     phone = db.Column(db.Unicode(16))
#     admin = db.Column(db.Boolean, default=False)
#     password = db.Column(db.Unicode(256))
#
#
# class Orders(db.Model):
#     order_id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey(Users.id))
#     address = db.Column(db.Unicode(128))


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.Unicode(16))
    admin = db.Column(db.Boolean, default=False)
    password = db.Column(db.Unicode(256), nullable=True)


class Order(db.Model):
    __tablename__ = "order"

    order_id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", backref=backref("orders", uselist=True))

    address = db.Column(db.Unicode(128))
