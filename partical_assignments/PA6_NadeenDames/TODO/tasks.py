from flask import Blueprint, render_template,request ,session, redirect
from TODO.db import get_db
import sqlite3
import datetime
# define our blueprint
bp = Blueprint('tasks', __name__)

@bp.route('/')
@bp.route('/tasks')
def index():
    
    # get the DB connection
    db = get_db()

    # retrieve all posts
    tasks = db.execute(
        'SELECT t.id, title, body,task_id,created,username'
        ' FROM task t JOIN user u ON t.id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()

    # render 'blog' blueprint with posts
    return render_template('task/index.html',tasks=tasks)

@bp.route('/add/task', methods = ['GET', 'POST'])
def add_task():
    if request.method == 'POST':

        # read post values from the form
        title = request.form['title']
        body = request.form['body-task']

        # read the 'uid' from the session for the current logged in user
        task_id = session['uid']

        # get the DB connection
        db = get_db()
        
        # insert post into database
        try:
            # execute the SQL insert statement
            db.execute("INSERT INTO task (task_id,title, body) VALUES (?,?,?);", (task_id ,title, body))
            
            # commit changes to the database
            db.commit()
            
            return redirect('/tasks') 

        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            return redirect("/404")
    else:
        # if the user is not logged in, redirect to '/login' 
        if "uid" not in session:
            return redirect('/login')
      
        # else, render the template
        return render_template("task/add-task.html")

@bp.route('/delete/tasks', methods=['GET', 'POST'])
def delete_tasks():
        # get the DB connection
        db = get_db()

        # insert user into db
        try:
            db.execute("DELETE FROM task")
            db.commit()
            
            return redirect("/tasks")

        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            return redirect("/404")
