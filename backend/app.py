from flask import Flask
from backend.core.database import db
from flask_migrate import Migrate

from backend.models import Player # noqa

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///game.db'

db.init_app(app)

migrate = Migrate(app, db)