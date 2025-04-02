from flask import Flask
from backend.core.database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///game.db'

db.init_app(app)