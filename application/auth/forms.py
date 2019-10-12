from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired, length
  
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), length(min=2, max=50)]) 
    password = PasswordField("Password", validators=[DataRequired(), length(min=2, max=50)])
  
    class Meta:
        csrf = False