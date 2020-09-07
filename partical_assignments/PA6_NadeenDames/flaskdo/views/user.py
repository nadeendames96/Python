import sqlite3
from flask import Blueprint, render_template, request, redirect, session, url_for
from ..db import get_db

bp=Blueprint("user",__name__)

@bp.route('/user/info')
@bp.route('/users')

def user_info():
    db=get_db()
    users=db.execute("SELECT * FROM User WHERE id=?;", (str(session['uid'],))).fetchall()
    return  render_template('user/user_info.html',users=users)



# Create User Update
@bp.route('/user/update',methods=['POST','GET'])
def user_update():
    if request.method=='GET':
        return render_template('user/user_update.html')

    else:
        firstname=request.form['firstname']
        lastname=request.form['lastname']
        username=request.form['username']
        email=request.form['email']
        password=request.form['password']
        user_pucture=request.form['user-picture']

        db=get_db()
        update=db.execute("UPDATE user SET firstname=?,lastname=?,username=?,email=?,password=?,picture=?;",(firstname,lastname,username,email,password,user_pucture))
        db.commit()
        return redirect('/users')