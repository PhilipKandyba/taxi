from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:490759Filosof@127.0.0.1:5432/taxi'
db = SQLAlchemy(app)

SESSION_TYPE = 'redis'
app.config.from_object(__name__)
Session(app)
migrate = Migrate(app, db)

db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
