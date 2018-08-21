from app import db
from app.models import User
from app.bl import user_exists, password_hash, get_user

from werkzeug.security import check_password_hash

from flask import session, url_for, jsonify


def admin_login(phone, password):
    admin = get_user(phone=phone, admin=True)

    if admin and check_password_hash(admin.password, password) is True:
        session['logged'] = True

        return jsonify({'status': 'Success',
                        'url': url_for('admin'),
                        })

    return jsonify({'error': 'User not found'})


def create_new_admin(phone, password):
    print(user_exists(phone))

    if user_exists(phone) is True:
        return jsonify({'error': "User exist"})

    hashed_password = password_hash(password)

    admin = User(phone=phone, password=hashed_password, admin=True)

    db.session.add(admin)
    db.session.commit()

    return jsonify({'status': "New admin was created"})
