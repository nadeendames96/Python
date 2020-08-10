from flask import Flask  # import flask
from flask import render_template
from flask import url_for

from contact import Contact
from contact_book import ContactBook
from data import generate_contacts

app = Flask(__name__)  # create a new flask application

# create a contact book
contact_book = generate_contacts()

# define basic routes
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/contacts')
def contacts():
    return render_template("contacts.html", contacts = contact_book.get_contacts())

@app.route('/contact/<int:contact_id>')
def contact(contact_id):
    return render_template("contact.html", contact = contact_book.get_contact(contact_id))

@app.route('/length')
def length():
    return str(len(contact_book.get_contacts()))


# run your flask application

if __name__ == "__main__":  # on running python app.py
    app.run(debug=True)  # run the flask app
