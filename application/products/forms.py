from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import IntegerField
from wtforms.validators import DataRequired

class NewProductForm(FlaskForm):
    name = StringField("Product name", validators=[DataRequired()])
    price = IntegerField("Price", validators=[DataRequired()])
 
    class Meta:
        csrf = False