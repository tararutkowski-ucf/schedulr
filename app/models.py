###########################################################
################## Database Models! #######################
###########################################################
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db, login
from flask_login import UserMixin

#To update db use flask-migrate and uprade. 
#in bash: flask db migrate -m "users table" [OR "contacts table"]
#Then run flask db upgrade

#How we want our databases to be modelled
#User class- needs id, username, email, and a hashed password
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    #Generates a hash for your password function
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    #Validates password function
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    #Formats how to represent in db
    def __repr__(self):
        return '<User {}>'.format(self.username)    

#Contact Class
class user_reqs(db.Model):
    userid = db.Column(db.Integer())
    rs_id = db.Column(db.Integer())

class reqsets(db.Model):
    rs_id = db.Column(db.Integer())
    name = db.Column(db.String())
    catalog_year = db.Column(db.Integer())

class requirements(db.Model):
    rs_id = db.Column(db.Integer())
    classid = db.Column(db.Integer())

class classes(db.Model):
    classid = db.Column(db.Integer())
    name = db.Column(db.String())
    course_code = db.Column(db.String())
    hours = db.Column(db.Integer())

class class_deps(db.Model):
    clas = db.Column(db.Integer())
    prereq = db.Column(db.Integer())

class classestaken(db.Model):
    usersid = db.Column(db.Integer())
    classid = db.Column(db.Integer())
    grade = db.Column(db.String())
    status = db.Column(db.String())


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
