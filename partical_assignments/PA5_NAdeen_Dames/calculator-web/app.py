from flask import Flask  # import flask
from flask import render_template
from flask import url_for

app = Flask(__name__)  # create a new flask application


@app.route('/')
def index():
    return render_template('calculator.html')




if __name__ == "__main__":  # on running python app.py
    app.run(debug=True)  # run the flask app
