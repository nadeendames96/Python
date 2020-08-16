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
    cookie.update_biography("Some quick example text to build on the card title and make up the bulk of the card's content.")

    # create contact for Don Music
    don = Contact("Don", "Music")

    # call add_label on don
    don.add_label("Music")
    don.add_label("Friend")

    # call add_phone on don
    don.add_phone("12345678", "work")

    # add avatar
    don.avatar_url = "https://vignette.wikia.nocookie.net/muppet/images/c/c3/Don_Music.png/revision/latest/scale-to-width-down/280?cb=20110808141055"
    
    # create contact for Roosevelt Franklin
    roosevelt = Contact("Roosevelt", "Franklin")

    # call add_phone on don
    roosevelt.add_phone("12345678", "personal")

    # call add_email() on roosevelt
    roosevelt.add_email("roosevelt@sesame.com")
    roosevelt.add_email("frankie@sesame.com")

    # set the avatar
    roosevelt.avatar_url = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmuppetmindset.files.wordpress.com%2F2014%2F06%2Froosevelt-franklin.png%3Fw%3D251%26h%3D300&f=1&nofb=1"

    # create contact for Bert
    bert = Contact("Bert", "Sesame")
    bert.add_email("bert@sesame.com")
    bert.add_label("Bert from Sesame")
    bert.add_label("Friends with Ernie")
    bert.update_biography("Bert is Ernie's best friend and roommate on Sesame Street. The pair share the basement apartment at 123 Sesame Street.")
    bert.avatar_url = "https://vignette.wikia.nocookie.net/muppet/images/e/e1/Bert_smile.png/revision/latest/scale-to-width-down/280?cb=20110630173259"

    # add contacts to contact book
    sesame_street.add(cookie)
    sesame_street.add(don)
    sesame_street.add(roosevelt)
    sesame_street.add(bert)

    return sesame_street