from application import db
from application.models import Base

from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"
  
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    orders = db.relationship('StoreOrder', backref='account', lazy=True)


    def __init__(self, username, password):
        self.username = username
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    @staticmethod
    def find_the_sum_of_spent_money_by_user(user_id):
        stmt = text("SELECT Store_Order.user_id, SUM(Product.price) FROM Store_Order"
                    " JOIN store_order_has_product ON Store_Order.id = store_order_has_product.store_order_id "
                    " JOIN product ON store_order_has_product.product_id = product.id "
                    " GROUP BY Store_Order.user_id "
                    " HAVING store_order.user_id = :user_id").params(user_id =  user_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response = row[1]

        return response