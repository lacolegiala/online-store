from application import db
from application.models import Base

class Product(Base):
    name = db.Column(db.String(144), nullable=False)
    price = db.Column(db.Integer, nullable=False)


    def __init__(self, name, price):
        self.name = name
        self.price = price

class StoreOrder(Base):
    user_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)