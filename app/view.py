from app import app
from app import db
from flask import render_template, request, jsonify, session, redirect, url_for
from app.models import User, Order
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/order', methods=['POST'])
def order():
    address = request.form['address']
    phone = request.form['phone']
    user = User(phone=phone)
    db.session.add(user)
    order = Order(address=address, user=user)
    db.session.add(order)
    db.session.commit()
    return render_template('from_form.html', order=order)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return redirect(url_for('admin'))


@app.route('/admin', methods=['GET'])
def admin():
    orders = Order.query.all()

    if not session.get('logged_in'):
        return redirect(url_for('login'))

    return render_template('admin.html', orders=orders)


@app.route('/login_in', methods=['POST'])
def login_in():
    phone = request.form['phone']
    password = request.form['password']

    user = User.query.filter_by(phone=phone, admin=True).first()

    if user and check_password_hash(user.password, password) is True:
        session['logged_in'] = True

        return jsonify({'status': 'Success'})

    return jsonify({'error': 'User not found'})


@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('login'))


@app.route('/create_admin&<phone>&<password>')
def create_admin(phone, password, secret):
    pw_hash = generate_password_hash(password)
    admin = User(phone=phone, password=pw_hash, admin=True)
    db.session.add(admin)
    db.session.commit()
