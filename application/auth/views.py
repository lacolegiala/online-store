from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from application import db

from application import app
from application.auth.models import User, Role
from application.auth.forms import LoginForm

from application import user_datastore

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/login.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/login.html", form = form,
                               error = "No such username or password")


    login_user(user)
    return redirect(url_for("index"))    

@app.route("/auth/logout")
def auth_logout():
  logout_user()
  return redirect(url_for("index"))

@app.route("/auth/register")
def auth_register():
  return render_template("auth/register.html", form = LoginForm())

@app.route("/auth/register", methods = ["POST"])
def auth_registered():
    form = LoginForm(request.form)

    if not form.validate():
        return render_template("auth/register.html", form = form)

    user = user_datastore.create_user(username=form.username.data, password=form.password.data)
    user_datastore.add_role_to_user(user, 'user')

    db.session().commit()

    login_user(user)

    return redirect(url_for("index"))

