import os

from flask import Flask,session,render_template,request,redirect
import sqlite3
from TODO.db import get_db

def create_app(test_config=None):
    # create the Flask
    app = Flask(__name__, instance_relative_config=True)

    # configure the app
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'blog.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/register',methods=['POST','GET'])
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
        


    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/logout',methods=['POST','GET'])
    def logout():
    # pop 'uid' from session
        session.pop("uid", None)
        # redirect to index
        return render_template("login/login.html")

    @app.route('/login', methods =['POST','GET'])
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


    # import helper DB functions
    from . import db
    db.init_app(app)

    # register the 'blog' blueprint
    from . import tasks
    app.register_blueprint(tasks.bp)

    # # register the 'user' blueprint
    from . import user
    app.register_blueprint(user.bp)

    # # register the 'task' blueprint
    from . import task
    app.register_blueprint(task.bp)

    
    return app