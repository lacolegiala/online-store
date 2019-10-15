from flask import render_template
from application import app
from application.products.models import Product, StoreOrder
from application.auth.models import User, Role
from flask_login import current_user
from flask import session

@app.route("/")
def index():

  productList = Product.order_by_bestselling(Product.query.all())

  return render_template("index.html", products = productList)