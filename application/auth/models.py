from application.db import db
from application.models import Base

from flask_security import RoleMixin

from sqlalchemy.sql import text

from flask_security.core import UserMixin

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('account.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)

class User(Base):

    __tablename__ = "account"
  
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    orders = db.relationship('StoreOrder', backref='account', lazy=True)
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))


    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def has_role(self, role):
        return role in self.roles

    @staticmethod
    def find_the_sum_of_spent_money_by_user(user_id):
        stmt = text("SELECT Store_Order.user_id, SUM(Product.price) FROM Store_Order"
                    " JOIN store_order_has_product ON Store_Order.id = store_order_has_product.store_order_id "
                    " JOIN product ON store_order_has_product.product_id = product.id "
                    " GROUP BY Store_Order.user_id "
                    " HAVING store_order.user_id = :user_id").params(user_id =  user_id)
        res = db.engine.execute(stmt)

        response = 0
        for row in res:
            response = row[1]

        return response