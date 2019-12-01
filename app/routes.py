from flask import render_template,redirect, url_for, request, jsonify, send_from_directory
from app import app, db, login
from flask_login import current_user, login_user, logout_user, login_required, UserMixin
from werkzeug.urls import url_parse


class User(UserMixin):
    id = 0
    def __init__(self,newId):
        self.id = newId

@login.user_loader
def load_user(id):
    return User(id)

@app.route('/assets/<path:filename>/')
def static_subdir(filename=None):
    print(filename);
    directory = 'assets'
    return send_from_directory(directory, filename)

@app.route('/', methods=['GET', 'POST'])
#@login_required
#Index is home page- where you can see your contacts
def index():

    return(render_template('index.html'))

    if current_user:
        return (current_user.id)
    else:
        return(0)

#This is the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    #If they are already logged in redirect to index
    if request.method == 'GET':
        return("Please login with a JSON POST")

    elif request.method == 'POST':
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        
        form = request.json

        with db.cursor() as cursor:
            sql = "Select ID FROM Users WHERE Username = %s and Password = sha2(%s,256)"
            cursor.execute(sql,(form['Username'],form['Password']))
            result = cursor.fetchall();
        
            if len(result) == 0:
                return jsonify({'User': 0})

            else:
                user = User(result[0][0])
                login_user(user, remember=form['Remember_Me'])
                return jsonify({'User': result[0][0]})
   

#Logout
@app.route('/logout')
def logout():
    #just use logout user function and redirect to login
    logout_user()
    return "Logged out"

#Register user
@app.route('/register', methods=['GET', 'POST'])
def register():
    #If user is logged in, redirect to index
    if current_user.is_authenticated:
        return redirect(url_for('index'))
        #Use registration form

    #If failed go to register page
    return "Register Page"

@app.route('/home', methods=['GET'])
def home():
    return "Home Page"

@app.route('/myinfo',methods = ['GET'])
@login_required
def myInfo():
    with db.cursor() as cursor:
        sql = "SELECT Username,FirstName,LastName,Email FROM Users WHERE ID=%s"
        cursor.execute(sql,(current_user.id))
        sqlOutput = cursor.fetchone()

        out = {}
        out['Username'] = sqlOutput[0]
        out['FirstName'] = sqlOutput[1]
        out['LastName'] = sqlOutput[2]
        out['Email'] = sqlOutput[3]

        return(jsonify(out))

@app.route('/myclasses',methods = ['GET'])
@login_required
def myClasses():
    with db.cursor() as cursor:
        sqlSelect0 = "Select Classes.Name, Classes.Code,Classes.Hours,Classes_Taken.YearTaken,"
        sqlSelect1 = "Classes_Taken.Semester, Classes_Taken.Grade "
        sqlFrom = "From Classes_Taken JOIN Classes ON Classes_Taken.ClassID = Classes.ID "
        sqlWhere = "Where Classes_Taken.UserID=%s"
        cursor.execute(sqlSelect0 + sqlSelect1 + sqlFrom + sqlWhere,(current_user.id))
        sqlOutput = cursor.fetchall()

        array = [];

        for item in sqlOutput:
            out = {}
            out['ClassName'] = item[0]
            out['ClassCode'] = item[1]
            out['Hours'] = item[2]
            out['Year'] = item[3]
            out['Semester'] = item[4]
            out['Grade'] = item[5]
            array.append(out)

        return(jsonify(array))

@app.route('/classes', methods=['GET'])
def classes():
    with db.cursor() as cursor:
        sql = "SELECT * FROM Classes"
        cursor.execute(sql)
        sqlOutput = cursor.fetchall()

        array = []

        for item in sqlOutput:
            line = {}
            line['ID'] = item[0]
            line['Code'] = item[1]
            line['Name'] = item[2]
            line['Hours'] = item[3]
            array.append(line)
        
        result = {'classes' : array,'count' : len(array)}
        return(jsonify(result))
