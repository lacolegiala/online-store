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

  return render_template("products/edit.html",
    product_id = product_id,
    product_name = product.name, 
    product_price = product.price
  )
  
@app.route("/products/<product_id>/", methods=["POST"])
def products_set_done(product_id):
    product = Product.query.get(product_id)
    product.price = request.form.get("price")
    product.name = request.form.get("name")
    db.session().commit()
  
    return redirect(url_for("products_index"))

@app.route("/products/", methods=["POST"])
def products_create():
    form = NewProductForm(request.form)

    if not form.validate():
      return render_template("products/new.html", form = form)

    t = Product(form.name.data, form.price.data)

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("products_index"))