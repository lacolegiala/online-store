from flask import render_template, request, redirect, url_for
from flask_login import current_user, logout_user
from application import db

from application import app
from application.auth.models import User
from application.users.forms import PasswordForm

from application import user_datastore

@app.route("/profile")
def profile_edit():
  return render_template("users/profile.html", form = PasswordForm())

@app.route("/profile", methods =["POST"])
def profile_edited():
  form = PasswordForm(request.form)

  if not form.validate():
    return render_template("users/profile.html", form = form)

  user = current_user
  user.password = form.password.data

  db.session().commit()

  return redirect(url_for("index"))

@app.route("/profile/delete", methods =["GET"])
def profile_delete():

  User.query.filter_by(id=current_user.id).delete()

  logout_user()
  db.session().commit()

  return redirect(url_for("index"))

