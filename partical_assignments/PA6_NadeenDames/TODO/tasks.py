from flask import Blueprint, render_template, abort,request,session,redirect
from jinja2 import TemplateNotFound
from TODO.models.tasklist import generate_tasklist_info
from TODO.db import get_db
import sqlite3
import datetime



bp = Blueprint('tasks', __name__)
tasklist=generate_tasklist_info()
@bp.route('/',methods=['POST','GET'])
@bp.route('/tasks',methods=['POST','GET'])
def index():
    if "uid" not in session:
            return redirect('/login')
   
    db=get_db()
    taskslist=db.execute(
        'SELECT id, tasklistname, tasklistdescription,tasklistphoto, created'
        ' FROM tasklist '
        ' ORDER BY created DESC ' )
    try:
        return render_template('tasks/index.html',taskslist=taskslist)
    except TemplateNotFound:
        abort(404)
            # if the user is not logged in, redirect to '/login' 
       
@bp.route('/add/tasklist',methods=['POST','GET'])
def add_taskslist():
    if "uid" not in session:
            return redirect('/login')
    if request.method=='GET':
        return render_template('tasks/addtaskslist.html')
    else:
        tasklistname=request.form['tasklist']
        tasklistdescription=request.form['tasklistdescription']
        upload_photo=request.form['photofile']
        # taskslist_id = session['uid']

        db=get_db()

        try:  
            # if "uid" not in session:
            # insert data into taskslist
            db.execute("INSERT INTO tasklist (tasklistname, tasklistdescription, tasklistphoto) VALUES (?, ?,?);", (tasklistname,tasklistdescription, upload_photo))
            # commit changes to the database
            db.commit()
            return redirect('/tasks') 

                # error
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            return redirect("/404")

@bp.route('/delete/taskslist')
def delete_tasks_list():
    if "uid" not in session:
            return redirect('/login')
    
    db=get_db()
    try:
        db.execute("DELETE FROM tasklist")
        db.commit()
        return redirect('/tasks')

    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        return redirect("/404")

@bp.route('/tasks/updateinfo',methods=['POST','GET'])
def updateinfo():
    if "uid" not in session:
            return redirect('/login')
    if request.method=='GET':
        return render_template('tasks/updateinfo.html')
    else:
        db=get_db()
        tasklist_title=request.form['tasklist_title']
        tasklist_description=request.form['task_description']
        tasklistphoto=request.form['tasklist_photo']

        try:
            db.execute("UPDATE tasks set tasklistname=?,tasklistdescription=?,tasklistphoto=?;",(tasklist_title,tasklist_description,tasklistphoto))
            db.commit()
            return redirect('/tasks')
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            return redirect("/404")
