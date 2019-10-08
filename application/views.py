from flask import render_template
from application import app
from application.products.models import Product

@app.route("/")
def index():
    return render_template("index.html", products = Product.query.all())