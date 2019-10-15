from application import db
from application.models import Base

from sqlalchemy.sql import text

class Product(Base):
    name = db.Column(db.String(144), nullable=False)
    price = db.Column(db.Integer, nullable=False)


    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def order_by_bestselling(cls, products):
        stmt = text("SELECT * FROM product"
                    " JOIN store_order_has_product ON product.id = store_order_has_product.product_id "
                    " GROUP BY store_order_has_product.product_id "
                    " ORDER BY COUNT(*) DESC")
        res = db.engine.execute(stmt)

        return res

store_order_has_product = db.Table('store_order_has_product',
    db.Column('store_order_id', db.Integer, db.ForeignKey('store_order.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True)
)

class StoreOrder(Base):
    user_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    products = db.relationship('Product', secondary=store_order_has_product, lazy='subquery',
        backref=db.backref('orders', lazy=True))

