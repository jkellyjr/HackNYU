from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, DateField
from wtforms.validators import DataRequired, Length, EqualTo


# login form
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


# user signup form
class SignUpForm(FlaskForm):
    first_name = StringField('First_Name', validators=[DataRequired(), Length(min=3, max=25)])
    last_name = StringField('Last_Name', validators=[DataRequired(), Length(min=3, max=25)])
    email = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)])
    phone = StringField('Phone_Number', validators=[DataRequired(), Length(min=10, max=10)])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm_password',
        message = 'Passwords must match')] )
    confirm_password = PasswordField('Repeat Password')
    therapist = BooleanField('Therapist', default = False)
    patient = BooleanField('Patient', default = False)
