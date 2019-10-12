from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore

from application.auth.models import User, Role
from application.db import db
from application.app import app

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

@app.before_first_request
def seed_roles():
  user_datastore.find_or_create_role('admin')
  user_datastore.find_or_create_role('user')

  adminUser = User.query.filter_by(username='admin').first()
  if not adminUser:
    adminUser = user_datastore.create_user(username='admin', password='1234567890')
    user_datastore.add_role_to_user(adminUser, 'admin')
  
  db.session.commit()


from application import views

from application.products import models
from application.products import views

from application.auth import views 

from application.users import views

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality"

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)

try:   
    db.create_all()
except:
    pass