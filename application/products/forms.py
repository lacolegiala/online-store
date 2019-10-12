from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import IntegerField
from wtforms.validators import DataRequired, NumberRange, length

class NewProductForm(FlaskForm):
    name = StringField("Product name", validators=[DataRequired(), length(min = 2, max = 100)])
    price = IntegerField("Price", validators=[NumberRange(min = 5, max = 100000)])
 
    class Meta:
        csrf = False