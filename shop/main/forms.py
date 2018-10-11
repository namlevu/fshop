from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, HiddenField, IntegerField, TextAreaField, PasswordField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
#from flask_babel import _, lazy_gettext as _l

class InstallForm(FlaskForm):
  fullname = StringField('Full name', validators=[DataRequired()])
  username = StringField('User name', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired()])
  password_hash = PasswordField('Password', validators=[DataRequired()])
  submit = SubmitField('Tạo User')
