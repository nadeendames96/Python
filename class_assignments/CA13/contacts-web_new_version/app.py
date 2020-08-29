import os
from flask import Flask, render_template, flash, redirect, url_for, Markup, request
from contact_book import ContactBook
from contact import Contact
from data import generate_contacts

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secret string')

# site wide settings
site = {
    'name':'Sesame Book'
}

# generate list of contacts
contact_book = generate_contacts()


@app.route('/')
def index():
    return render_template('index.html', contact_book=contact_book, site = site)

@app.route('/contacts/list')
def contacts():
    return render_template('contacts.html', contacts = contact_book.get_contacts(), site = site)

@app.route('/contacts/card')
def contacts_card():
    return render_template('contacts-card.html', contacts = contact_book.get_contacts(), site = site)

@app.route('/contacts/add', methods=['POST', 'GET'])
def add_contact():
    print("Called")
    if request.method == 'GET':
        return render_template('add-contact.html', site = site)
    if request.method == 'POST':
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        biography = request.form['biography']
        avatar = request.form['avatar']

        contact = Contact(first_name, last_name)

        if biography != "":
            contact.update_biography(biography)
        if avatar != "":
            contact.avatar_url = avatar
            
        contact_book.add(contact)

        return redirect(url_for('contacts'))

@app.route('/contact/<int:contact_id>')
def get_contact(contact_id):
    contact = contact_book.get_contact(contact_id)
    return render_template('contact.html', contact = contact, site = site)

@app.route('/contact/delete/<int:contact_id>')
def delete_contact(contact_id):
    contact_book.delete_contact(contact_id)
    return redirect(url_for('contacts'))

@app.route('/phone/add/<int:contact_id>', methods=['POST'])
def add_phone(contact_id):

    # read the values from the modal form
    phone_number = request.form['phoneNumber']
    label = request.form['label']

    # add phone number to the contact   
    contact = contact_book.get_contact(contact_id)
    contact.add_phone(phone_number, label)

    # render the contact again
    return render_template('contact.html', contact = contact, site = site )

@app.route('/email/add/<int:contact_id>', methods=['POST'])
def add_email(contact_id):
    email = request.form['email']

    # retrieve the contact and add the email
    contact = contact_book.get_contact(contact_id)
    contact.add_email(email)

    return redirect(url_for('get_contact', contact_id = contact.id , site = site))

@app.route('/label/add/<int:contact_id>', methods=['GET','POST'])
def add_label(contact_id):

    contact = contact_book.get_contact(contact_id)

    if request.method == 'GET':
        return render_template('add-label.html', site=site, contact_id = contact_id, contact= contact)

    if request.method == 'POST':
        # read the label from the form submission
        label = request.form['label']
        
        # add the label to the user
        contact.add_label(label)

        return redirect(url_for('get_contact', contact_id = contact_id, contact = contact, site = site))


# register template global function
@app.template_global()
def global_message():
    return 'I am global message.'


# register template filter
# @app.template_filter()
# def musical(s):
#     return s + Markup(' &#9835;')



# message flashing
@app.route('/flash')
def just_flash():
    flash('I am Flash, who is looking for me?')
    # flash('I am Flash, again.')

    return redirect(url_for('index'))


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
