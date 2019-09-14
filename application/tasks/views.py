from application import app, db
from flask import redirect, render_template, request, url_for
from application.tasks.models import Product

@app.route("/tasks", methods=["GET"])
def tasks_index():
    return render_template("tasks/list.html", tasks = Product.query.all())

@app.route("/tasks/new/")
def tasks_form():
    return render_template("tasks/new.html")
  
@app.route("/tasks/<task_id>/", methods=["POST"])
def tasks_set_done(task_id):

    product = Product.query.get(task_id)
    product.price = 1000
    db.session().commit()
  
    return redirect(url_for("tasks_index"))

@app.route("/tasks/", methods=["POST"])
def tasks_create():
    t = Product(request.form.get("name"), 2000)

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("tasks_index"))