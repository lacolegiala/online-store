from application import app, db
from flask import redirect, render_template, request, url_for
from application.products.models import Product

@app.route("/products", methods=["GET"])
def products_index():
    return render_template("products/list.html", products = Product.query.all())

@app.route("/products/new/")
def products_form():
    return render_template("products/new.html")

@app.route("/products/edit/<product_id>")
def products_edit(product_id):
  return render_template("products/edit.html", product_id = product_id)
  
@app.route("/products/<product_id>/", methods=["POST"])
def products_set_done(product_id):

    product = Product.query.get(product_id)
    product.price = 1000
    db.session().commit()
  
    return redirect(url_for("products_index"))

@app.route("/products/", methods=["POST"])
def products_create():
    t = Product(request.form.get("name"), request.form.get("price"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("products_index"))