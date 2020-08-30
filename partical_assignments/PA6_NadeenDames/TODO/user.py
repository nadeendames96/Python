import sqlite3
from flask import Blueprint, render_template, request, redirect,session
from TODO.db import get_db

# define our blueprint
bp = Blueprint('user', __name__)


@bp.route('/add/user', methods=['GET', 'POST'])
def add_user():
    
    if request.method == 'GET':
        # render add user blueprint
        return render_template('user/index.html')
    else:
        username = request.form['username']
        password = request.form['password']

        # get the DB connection
        db = get_db()

        # insert user into db
        try:
            db.execute("INSERT INTO user (username, password) VALUES (?, ?);", (username, password))
            db.commit()
            
            return redirect("/users")

        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            return redirect("/404")

@bp.route('/users')
def get_users():
    # get the DB connection
    db = get_db()

    # insert user into db
    users = db.execute('select * from user').fetchall()

    # render 'list.html' blueprint with users
    return render_template('user/list.html', users=users)

@bp.route('/delete')
def delete():
      
        db = get_db()
        # insert user into db
        try:
            db.execute('DELETE FROM user')
            db.commit()
            
            return render_template("login/login.html")

        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            return redirect("/404")
@bp.route('/user/update')
def update_username():
    if request.method == 'GET':
        # render add user blueprint
        return render_template('user/update-username.html')
    else:
        username = request.form['username_update']
        # get the DB connection
        db = get_db()

        # insert user into db
        try:
            db.execute("UPDATE  user SET username=?",(username))
            db.commit()

            return redirect("/users")

        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            return redirect("/404")
@bp.route('/user/update/email')
def update_email():
    if request.method == 'GET':
        # render add user blueprint
        return render_template('user/update-email.html')
    else:
        email = request.form['email_update']
        # get the DB connection
        db = get_db()

        # insert user into db
        try:
            db.execute("UPDATE  user SET email=?",(email))
            db.commit()
            
            return redirect("/users")

        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            return redirect("/404")

@bp.route('/user/update')
def update_password():
    if request.method == 'GET':
        # render add user blueprint
        return render_template('user/update-password.html')
    else:
        password = request.form['password_update']
        # get the DB connection
        db = get_db()

        # insert user into db
        try:
            db.execute("UPDATE  user SET password=?",(password))
            db.commit()
            
            return redirect("/users")

        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            return redirect("/404")
