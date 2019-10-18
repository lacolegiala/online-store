from application import db
from application.models import Base

from sqlalchemy.sql import text

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

    @staticmethod 
    def get_revenue():
        stmt = text("SELECT SUM(price) FROM product"
                    " JOIN store_order_has_product ON product.id = store_order_has_product.product_id"
                    " JOIN store_order ON store_order_has_product.store_order_id = store_order.id")
        res = db.engine.execute(stmt)

        response = 0
        for row in res:
            response = row[0]

        return response

