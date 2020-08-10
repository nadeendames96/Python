from contact import Contact
from contact_book import ContactBook

def generate_contacts():

    # create a contact book
    sesame_street = ContactBook()

    # create contact for Cookie Monster
    cookie = Contact("Cookie", "Monster")

    # call add_phone() on cookie
    cookie.add_phone("12345678", "work")
    cookie.add_phone("00123456", "Cookie Line")
    cookie.add_label("Cookie")
    cookie.add_label("Friend")

    cookie.add_email("cookie@monters.com")

    # create contact for Don Music
    don = Contact("Don", "Music")

    # call add_label on don
    don.add_label("Music")
    don.add_label("Friend")

    # call add_phone on don
    don.add_phone("12345678", "work")

    # create contact for Roosevelt Franklin
    roosevelt = Contact("Roosevelt", "Franklin")

    # call add_phone on don
    roosevelt.add_phone("12345678", "personal")

    # call add_email() on roosevelt
    roosevelt.add_email("roosevelt@sesame.com")
    roosevelt.add_email("frankie@sesame.com")

    # add contacts to contact book
    sesame_street.add(cookie)
    sesame_street.add(don)
    sesame_street.add(roosevelt)

    return sesame_street