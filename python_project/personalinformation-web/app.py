from flask import Flask,redirect,render_template,url_for,request,sessions
from personalinfo import PersonalInfo
from data import generate_data
import os

personalinfo=generate_data()
app=Flask( __name__ )
app.secret_key = os.getenv('SECRET_KEY', 'secret string')

# fullname={
#     'firstname':'Nadeen',
#     'lastname':'Dames'
# }

# Index 
@app.route('/')
def index():
    
    return render_template('index.html',personalinfo=personalinfo)
# About 
@app.route('/about')
def about(): 
    return render_template('about.html',personalinfo=personalinfo)

# Education 
@app.route('/eduction')
def education(): 
    return render_template('education.html',personalinfo=personalinfo)

# Experiance
@app.route('/experiance')
def experiance(): 
    return render_template('experiance.html',personalinfo=personalinfo)
# Internships 
@app.route('/internship')
def internship(): 
    return render_template('internships.html',personalinfo=personalinfo)
# Skills 
@app.route('/skill')
def skill(): 
    return render_template('skills.html',personalinfo=personalinfo)
@app.route('/certificate')
def certificate():
   return  render_template('certificate.html',personalinfo=personalinfo)
# 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


# 500 error handler
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500


# run your flask application
if __name__ == "__main__":  # on running python app.py
    app.run(debug=True)  # run the flask app
