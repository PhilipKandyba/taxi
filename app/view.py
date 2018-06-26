from app import app
from app import db
from flask import render_template, request, jsonify
from models import Users
from werkzeug.security import check_password_hash


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/order', methods=['POST'])
def order():
    address = request.form['address']
    phone = request.form['phone']
    user = Users(phone=phone, address=address)
    db.session.add(user)
    db.session.commit()
    return render_template('from_form.html', address=address, phone=phone)


@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('login.html')


@app.route('/list', methods=['GET'])
def list_page():
    users = Users.query.all()
    return render_template('list.html', users=users)


@app.route('/login_in', methods=['POST'])
def login_in():
    phone = request.form['phone']
    password = request.form['password']

    user = Users.query.filter_by(phone=phone, admin=True).scalar()

    if user and check_password_hash(user.password, password) is True:
        return jsonify({'status': 'Success'})

    return jsonify({'error': 'User not found'})
