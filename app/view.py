from app import app, db
from app.models import User
from app.options import is_logged
from app.bl import user_exists, get_user, new_user, do_order, orders_list

from werkzeug.security import generate_password_hash, check_password_hash

from flask import render_template, request, jsonify, session, redirect, url_for


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/order', methods=['POST'])
def new_order():
    address = request.form['address']
    phone = request.form['phone']

    if user_exists is True:
        user = get_user(phone=phone)
    else:
        user = new_user(phone=phone)

    order = do_order(address=address, user=user)

    return render_template('new_order.html', new_order=order)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/admin', methods=['GET'])
def admin():
    if is_logged() is False:
        return redirect(url_for('login'))

    orders = orders_list()

    return render_template('admin.html', orders=orders)


@app.route('/login_in', methods=['POST'])
def login_in():
    phone = request.form['phone']
    password = request.form['password']

    user = User.query.filter_by(phone=phone, admin=True).first()

    if user and check_password_hash(user.password, password) is True:
        session['logged'] = True

        return jsonify({'status': 'Success'})

    return jsonify({'error': 'User not found'})


@app.route('/new_admin')
def new_admin():
    if is_logged() is False:
        return redirect(url_for('login'))

    return render_template('create_admin.html')


@app.route('/create_admin', methods=['POST'])
def create_admin():
    phone = request.form['adm_phone']
    password = request.form['adm_password']
    conf_password = request.form['adm_password_confirmation']

    if password != conf_password:
        return jsonify({'error': "Confirmation incorrect"})

    if User.query.filter_by(phone=phone).first() is not None:
        return jsonify({'error': "User exist"})

    pw_hash = generate_password_hash(password)

    new_admin = User(phone=phone, password=pw_hash, admin=True)

    db.session.add(new_admin)
    db.session.commit()

    return jsonify({'status': "New admin was created"})


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store"
    return response


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))
