from app import app
from app.options import is_logged
from app.bl import user_exists, get_user, new_user, do_order, orders_list


from flask import render_template, request, session, redirect, url_for

from app.admin import create_new_admin, admin_login


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

    return admin_login(phone=phone, password=password)


@app.route('/new_admin')
def new_admin():
    if is_logged() is False:
        return redirect(url_for('login'))

    return render_template('create_admin.html')


@app.route('/create_admin', methods=['POST'])
def create_admin():
    phone = request.form['adm_phone']
    password = request.form['adm_password']

    return create_new_admin(phone=phone, password=password)



@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store"
    return response


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))
