from application import app, db
from flask import redirect, render_template, request, url_for
from application.products.models import Product
from application.products.forms import NewProductForm

@app.route("/products", methods=["GET"])
def products_index():
    return render_template("products/list.html", products = Product.query.all())

@app.route("/products/new/")
def products_form():
    return render_template("products/new.html", form = NewProductForm())

@app.route("/products/edit/<product_id>")
def products_edit(product_id):
  product = Product.query.get(product_id)
  form = NewProductForm()
  form.name.data = product.name
  form.price.data = product.price

  return render_template("products/edit.html", form = form, product_id = product_id)
  
@app.route("/products/<product_id>/", methods=["POST"])
def products_set_done(product_id):
    form = NewProductForm(request.form)

    if not form.validate():
      return render_template("products/edit.html", form = form)

    product = Product.query.get(product_id)
    product.price = form.price.data
    product.name = form.name.data

    db.session().commit()
  
    return redirect(url_for("products_index"))

@app.route("/products/", methods=["POST"])
def products_create():
    form = NewProductForm(request.form)

    if not form.validate():
      return render_template("products/new.html", form = form)

    product = Product(form.name.data, form.price.data)

    db.session().add(product)
    db.session().commit()
  
    return redirect(url_for("products_index"))