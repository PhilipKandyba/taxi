from app import app
from app import db
from flask import render_template, request
from models import Users
from werkzeug.security import check_password_hash


@app.route('/')
def index():
    users = Users.query.all()
    return render_template('index.html', users=users)


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
    if request.method == "POST":
        phone = request.form['phone']
        if db.session.query(Users).filter_by(phone=phone, admin=True).scalar():
            return render_template('index.html')
        else:
            return '<h1>Error</h1>'
    return render_template('login.html')


@app.route('/login_in', methods=['POST'])
def login_in():
    phone = request.form['phone']
    password = request.form['password']

    user = Users.query.filter_by(phone=phone, admin=True).scalar()

    if check_password_hash(user.password, password) is True:
        return 'Admin'
    else:
        return 'Error'
