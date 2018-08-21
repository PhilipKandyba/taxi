from app import db
from app.models import User, Order

from werkzeug.security import generate_password_hash


def user_exists(phone):
    return db.session.query(db.exists().where(User.phone == phone)).scalar()


def get_user(phone, admin=False):
    return User.query.filter_by(phone=phone, admin=admin).first()


def new_user(phone):
    return User(phone=phone)


def do_order(address, user):
    order = Order(address=address, user=user)

    db.session.add(order)
    db.session.commit()

    return order


def orders_list():
    list = Order.query.all()

    return list


def password_hash(password):
    return generate_password_hash(password)
