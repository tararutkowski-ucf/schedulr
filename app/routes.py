from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm, ContactForm, SearchForm, DeleteForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Contact
from werkzeug.urls import url_parse

@app.route('/', methods=['GET', 'POST'])
@login_required
#Index is home page- where you can see your contacts
def index():

    #User is current_user's username
    user = User.query.filter_by(username=current_user.username).first_or_404()
    #Search contacts for only that user's
    contacts = Contact.query.filter_by(owner=current_user.username)
    results = []
    for contact in contacts:
    	results.append(contact)

    results.sort(key=sortFirst)
    #Load up the template for index
    form = SearchForm(request.form)
    if request.method == 'POST':
        return search_results(form)
    return render_template('index.html', title='Home', form=form, user=user, contacts=results)

#This is the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    #If they are already logged in redirect to index
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    #Use a login form
    form = LoginForm()
    #If form is filled out correctly do this:
    if form.validate_on_submit():
        #Search db for username
        user = User.query.filter_by(username=form.username.data).first()
        #Check to see if password matches and if username in db
        if user is None or not user.check_password(form.password.data):
            #if not redirect to the login page to try again and give error
            flash('Invalid username or password')
            return redirect(url_for('login'))
        #Login the user and set remmeber = boolean from box
        login_user(user, remember=form.remember_me.data)
        #Redirect to index if logged in successfully
        return redirect(url_for('index'))
    #If form isnt filled out correctly redirect to login page to try again
    return render_template('login.html', title='Sign In', form=form)

#Logout
@app.route('/logout')
def logout():
    #just use logout user function and redirect to login
    logout_user()
    return redirect(url_for('login'))

#Register user
@app.route('/register', methods=['GET', 'POST'])
def register():
    #If user is logged in, redirect to index
    if current_user.is_authenticated:
        return redirect(url_for('index'))
        #Use registration form
    form = RegistrationForm()
    #if form works
    if form.validate_on_submit():
        #Set user and password and add to db
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        #congrats message and redirect to login
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    #If failed go to register page
    return render_template('register.html', title='Register', form=form)



       
