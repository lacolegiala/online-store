from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.products.models import Product, StoreOrder
from application.auth.models import User
from application.products.forms import NewProductForm
from flask_security.decorators import roles_required

@app.route("/products", methods=["GET"])
@roles_required('admin')
def products_index():
    return render_template("products/list.html", products = Product.query.all(), revenue = StoreOrder.get_revenue())

@app.route("/products/new/")
@roles_required('admin')
def products_form():
    return render_template("products/new.html", form = NewProductForm())

@app.route("/products/edit/<product_id>")
@roles_required('admin')
def products_edit(product_id):
  product = Product.query.get(product_id)
  form = NewProductForm()
  form.name.data = product.name
  form.price.data = product.price

  return render_template("products/edit.html", form = form, product_id = product_id)
  
@app.route("/products/<product_id>/", methods=["POST"])
@roles_required('admin')
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
@roles_required('admin')
def products_create():
    form = NewProductForm(request.form)

    if not form.validate():
      return render_template("products/new.html", form = form)

    product = Product(form.name.data, form.price.data)

    db.session().add(product)
    db.session().commit()
  
    return redirect(url_for("products_index"))

@app.route("/products/remove/<product_id>", methods=["GET"])
@roles_required('admin')
def products_remove(product_id):
  Product.query.filter_by(id=product_id).delete()

  db.session().commit()

  return redirect(url_for("products_index"))

@app.route("/products/order", methods=["POST"])
@login_required
def products_order():
  if len(request.form.getlist('orderProduct')) == 0:
    return render_template("index.html", products = Product.query.all(), error = "You must select at least 1 item")

  order = StoreOrder(user_id=current_user.id)
  
  user = User.query.filter_by(id=current_user.id).first()
  user.orders.append(order)
  
  products = Product.query.filter(Product.id.in_(request.form.getlist('orderProduct'))).all()
  
  for product in products:
    order.products.append(product)

  db.session().add(order)
  db.session().commit()

  return redirect(url_for("my_orders"))

@app.route("/myorders", methods=["GET"])
@login_required
def my_orders():

  orders = StoreOrder.query.filter_by(user_id=current_user.id).order_by(StoreOrder.date_created.desc())
  user_id = current_user.id

  return render_template("orders/myorders.html", orders = orders, i_have_spent=User.find_the_sum_of_spent_money_by_user(user_id))


