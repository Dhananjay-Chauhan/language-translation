from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config['SECRET_KEY'] = "dingdingdingdingding"
db = SQLAlchemy(app)

from .routes import *
# with app.app_context():
#     db.create_all()
