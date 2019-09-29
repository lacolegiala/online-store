from application import db
from application.models import Base

class Product(Base):
    name = db.Column(db.String(144), nullable=False)
    price = db.Column(db.Integer, nullable=False)


    def __init__(self, name, price):
        self.name = name
        self.price = price

store_order_has_product = db.Table('store_order_has_product',
    db.Column('store_order_id', db.Integer, db.ForeignKey('store_order.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True)
)

class StoreOrder(Base):
    user_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    products = db.relationship('Product', secondary=store_order_has_product, lazy='subquery',
        backref=db.backref('orders', lazy=True))
