from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:490759Filosof@127.0.0.1:5432/taxi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)

SESSION_TYPE = 'redis'
app.config.from_object(__name__)
Session(app)

from app.models import User

db.create_all()


from app.view import *

if __name__ == '__main__':
    app.run(debug=True)
