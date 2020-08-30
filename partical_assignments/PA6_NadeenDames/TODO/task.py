from flask import Blueprint, render_template, abort,request,session,redirect
from jinja2 import TemplateNotFound
from TODO.db import get_db
import sqlite3
import datetime
bp = Blueprint('task', __name__)
@bp.route('/task',methods=['POST','GET'])
def index():
    if "uid" not in session:
            return redirect('/login')
    
    db=get_db()
    tasks=db.execute(
        'SELECT id,task_id,created, title,body,prorites'
        ' FROM task '
        ' ORDER BY created DESC ' )
    try:
        return render_template('task/index.html',tasks=tasks)
    except TemplateNotFound:
        abort(404)
@bp.route('/add/task', methods = ['GET', 'POST'])
def add_task():
    if "uid" not in session:
            return redirect('/login')
    
    if request.method == 'POST':

        # read post values from the form
        title = request.form['tasktitle']
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
            
            return render_template('task/add-task.html') 

        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            return redirect("/404")
    else:
        # if the user is not logged in, redirect to '/login' 
        if "uid" not in session:
            return redirect('/login')
      
        # else, render the template
        return render_template("task/add-task.html")


@bp.route('/task/deletetask',methods=['POST','GET'])
def delete_task():
    if "uid" not in session:
            return redirect('/login')
    
    try:
        task_id=session['uid']
        db=get_db()
        db.execute("DELETE task_id FROM task WHERE task_id=(?);",(task_id))
        db.commit()
        return render_template("tasks/index.html")

    except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            return redirect("/404")

@bp.route('/task/updatetask',methods=['POST','GET'])
def update_task():
    if "uid" not in session:
            return redirect('/login')
    if request.method=='GET':
        return render_template('task/updatetask.html')
    else:
        db=get_db()
        tasktitle_update=request.form['tasktitle_update']
        taskbody_update=request.form['taskbody_update']
        prorites=request.form['prorites']
        # tasklist=request.form['tasklist']
        # task_id=session['uid']
        try:
            db.execute("UPDATE task set title=?,body=?,prorites=?,password=?;",(tasktitle_update,taskbody_update,prorites))
            db.commit()
            return render_template('task/updatetask.html')
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            return redirect("/404")
