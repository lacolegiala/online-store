from flask import render_template
from application import app
from application.products.models import Product
from application.auth.models import User, Role
from flask_login import current_user
from flask import session

@app.route("/")
def index():
    return render_template("index.html", products = Product.query.all())