from app import app
from app import db
from flask import render_template, request, jsonify, session, redirect, url_for
from models import User, Order
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/order', methods=['POST'])
def new_order():
    address = request.form['address']
    phone = request.form['phone']

    if User.query.filter_by(phone=phone).first() is not None:
        user = User.query.filter_by(phone=phone).first()
    else:
        user = User(phone=phone)

    order = Order(address=address, user=user)

    db.session.add(order)
    db.session.commit()

    return render_template('new_order.html', order=order)


@app.route('/login')
def login():
    if not session.get('logged'):
        return render_template('login.html')
    else:
        return redirect(url_for('admin'))


@app.route('/admin', methods=['GET'])
def admin():
    orders = Order.query.all()

    if not session.get('logged'):
        return redirect(url_for('login'))

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


@app.route('/logout')
def logout():
    session['logged'] = False
    return redirect(url_for('login'))


@app.route('/new_admin')
def new_admin():
    if not session.get('logged'):
        return redirect(url_for('login'))

    return render_template('create_admin.html')


@app.route('/create_admin', methods=['POST'])
def create_admin():
    phone = request.form['adm_phone']
    password = request.form['adm_password']

    pw_hash = generate_password_hash(password)

    new_admin = User(phone=phone, password=pw_hash, admin=True)

    db.session.add(new_admin)
    db.session.commit()

    return 'New admin with phone {0} - is created!'.format(phone)
