import sqlite3
from flask import Blueprint, render_template, request, redirect, session, url_for
from ..db import get_db

bp=Blueprint("user",__name__)

@bp.route('/user/info')
def user_info():
    db=get_db()
    users=db.execute("SELECT * FROM User WHERE id=?;", (str(session['uid'],))).fetchall()
    return  render_template('user/user_info.html',users=users)



# Create User Update