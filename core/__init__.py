from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from deep_translator import GoogleTranslator

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config['SECRET_KEY'] = "dingdingdingdingding"
db = SQLAlchemy(app)

trans = GoogleTranslator(source='en', target='es')


from .routes import *
# with app.app_context():
#     db.create_all()
