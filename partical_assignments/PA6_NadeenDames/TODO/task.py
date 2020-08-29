import sqlite3
from flask import Blueprint, render_template, request, redirect
from TODO.db import get_db

# define our blueprint
bp = Blueprint('task', __name__)


@bp.route('/add/task', methods=['GET', 'POST'])
def add_task():
    
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
def get_tasks():
    # get the DB connection
    db = get_db()

    # insert user into db
    users = db.execute('select * from user').fetchall()

    # render 'list.html' blueprint with users
    return render_template('user/list.html', users=users)
