from app import db
from app.models import User, Order

from werkzeug.security import check_password_hash
from flask import jsonify, session, url_for


def user_exists(phone):
    return db.session.query(db.exists().where(User.phone == phone))


def get_user(phone, admin=False):
    return User.query.filter_by(phone=phone, admin=admin).first()


def new_user(phone):
    return User(phone=phone)


def admin_login(phone, password):
    admin = get_user(phone=phone, admin=True)

    if admin and check_password_hash(admin.password, password) is True:
        session['logged'] = True

        return jsonify({'status': 'Success',
                        'url': url_for('admin'),
                        })

    return jsonify({'error': 'User not found'}), 400


def do_order(address, user):
    order = Order(address=address, user=user)

    db.session.add(order)
    db.session.commit()

    return order


def orders_list():
    list = Order.query.all()

    return list
