import sqlite3
from flask import Blueprint, render_template, request, redirect,session
from TODO.db import get_db

# define our blueprint
bp = Blueprint('user', __name__)


@bp.route('/add/user', methods=['GET', 'POST'])
def add_user():
    if "uid" not in session:
            return redirect('/login')

    if request.method == 'GET':
        # render add user blueprint
        return render_template('login/register.html')
    else:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        firstname = request.form['firstname']
        lastname = request.form['lastname']

        # get the DB connection
        db = get_db()

        # insert user into db
        try:
            db.execute("INSERT INTO user (username,fname,lname, password,email) VALUES (?, ?,?,?,?);", (username,firstname,lastname,password,email))
            db.commit()
            
            return redirect("/users")

        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            return redirect("/404")

@bp.route('/users')
def get_users():
    if "uid" not in session:
            return redirect('/login')
    # get the DB connection
    db = get_db()

    # insert user into db
    users = db.execute('select * from user').fetchall()

    # render 'list.html' blueprint with users
    return render_template('user/list.html', users=users)

@bp.route('/users/updateinfo',methods=['POST','GET'])
def updateinfo():
    if "uid" not in session:
            return redirect('/login')
    if request.method=='GET':
        return render_template('user/updateinfo.html')
    else:
        db=get_db()
        username=request.form['username']
        firstname=request.form['firstname']
        lastname=request.form['lastname']
        email=request.form['email']
        password=request.form['password']

        try:
            db.execute("UPDATE user set username=?,fname=?,lname=?,email=?,password=?;",(username,firstname,lastname,email,password))
            db.commit()
            return redirect('/users')
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            return redirect("/404")

@bp.route('/users/deleteuser')
def deleteaccount():
        if "uid" not in session:
            return redirect('/login')
        db=get_db()
        try:
            db.execute("DELETE FROM user")
            db.commit()
            return render_template('login/register.html')
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            return redirect("/404")
         