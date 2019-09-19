from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import IntegerField
from wtforms.validators import DataRequired
from wtforms.validators import NumberRange

class NewProductForm(FlaskForm):
    name = StringField("Product name", validators=[DataRequired()])
    price = IntegerField("Price", validators=[NumberRange(min = 5, max = 100000)])
 
    class Meta:
        csrf = False