import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    #Need secret key to prevent CSURF
    #CSURF Protection is needed to use flask wtf's flask forms
    #We used these in forms.py -> we can disable csurf requirement but it makes it less secure
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'

    #This is Database stuff
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
