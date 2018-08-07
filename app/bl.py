from app import db
from app.models import User, Order


def user_exists(phone):
    return db.session.query(db.exists().where(User.phone == phone))


def get_user(phone):
    return User.query.filter_by(phone=phone).first()


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
