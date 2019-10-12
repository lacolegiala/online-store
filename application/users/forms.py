from flask_wtf import FlaskForm
from wtforms import PasswordField
from wtforms.validators import DataRequired, length
  
class PasswordForm(FlaskForm):
    password = PasswordField("Password", validators=[DataRequired(), length(min=2, max=50)])
  
    class Meta:
        csrf = False