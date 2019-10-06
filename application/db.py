from flask_sqlalchemy import SQLAlchemy
import os
from os import urandom

from application.app import app

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///products.db"    
    app.config["SQLALCHEMY_ECHO"] = True

app.config["SECRET_KEY"] = urandom(32)

db = SQLAlchemy(app)