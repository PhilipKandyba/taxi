from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:490759Filosof@127.0.0.1:5432/taxi'

db = SQLAlchemy(app)
