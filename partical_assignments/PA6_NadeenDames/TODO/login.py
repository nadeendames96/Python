from flask import Blueprint, render_template,request ,redirect,session
from TODO.db import get_db
import sqlite3

# define our blueprint
bp = Blueprint('login', __name__)

@bp.route('/login', methods =['POST','GET'])
def login():
    if request.method == "GET":
        # render the login template
        return render_template('login/login.html')
    else:
        # read values from the login form
        username= request.form['username']
        password = request.form['password']

        # get the DB connection
        db = get_db()
        
        # insert user into db
        try:
            user= db.execute('SELECT * FROM user WHERE username LIKE ?',(username,)).fetchone()
            if user  != None:
                if user['username'] == username and user['password'] == password :  
                    session['uid']= user['id']  
                    return redirect("/tasks")

        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            return redirect("/404")

@bp.route('/register',methods=['POST','GET'])
def register():
    if request.method == "GET":
        # render the login template
        return render_template('login/register.html')
    else:
        # read values from the login form
        username= request.form['username']
        password = request.form['password']
        email = request.form['email']


        # get the DB connection
        db = get_db()
        
        # insert user into db
        try:
            db.execute("INSERT INTO user (username, password,email) VALUES (?, ?,?);", (username, password,email))
            db.commit()
            return redirect("/users")

        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            return redirect("/404")
    

@bp.route('/logout',methods=['POST','GET'])
def logout():
    # pop 'uid' from session
    session.pop("uid", None)

    # redirect to index
    return render_template("login/login.html")