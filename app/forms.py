from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, validators, BooleanField
from wtforms.validators import InputRequired, Email


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired(), validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    firstname = StringField('First Name', validators=[InputRequired()])
    lastname = StringField('Last Name', validators=[InputRequired()])
    trn = StringField('TRN', validators=[InputRequired()])
    gender = SelectField(u'Gender', choices=[('Male', 'Male'), ('Female', 'Female')])
    email = StringField('Email', validators=[InputRequired(), Email()])
    remember_me = BooleanField("Remember me?", default=True)