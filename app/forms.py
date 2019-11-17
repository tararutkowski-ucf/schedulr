###########################################################
######################## Forms! ###########################
###########################################################
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, StringField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User


#Login form - needs username, password, remember me button, submit button
class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')

#Registration Form- needs username, email. password, password verification, submit button
class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Register')

	#Functions to validate
	#Validate username checks to see if the username is already taken
	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError('Username already taken: Please use a different username.')

	#Validate email checks to see if email is already taken
	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is not None:
			raise ValidationError('Email already taken: Please log in or use a different email address.')

#Contact form- needs firstname, lastname, email, phone, and submit button
class ContactForm(FlaskForm):
	firstname = StringField('First Name', validators=[DataRequired()])
	lastname = StringField('Last Name', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	phone = IntegerField('Phone')
	submit = SubmitField('Add Contact')

class DeleteForm(FlaskForm):
	idnumber = IntegerField('idnumber')

#Search form
class SearchForm(FlaskForm):
    choices = [('First Name', 'First Name'),('Last Name', 'Last Name'),('Email', 'Email'),('Phone', 'Phone')]
    select = SelectField('Search contacts:', choices=choices)
    search = StringField('')
