from contact import Contact
from contact_book import ContactBook

# create contact for Cookie Monster
cookie = Contact("Cookie", "Monster")

# call add_phone() on cookie
cookie.add_phone("12345678", "work")
cookie.add_phone("00123456", "Cookie Line")
cookie.add_label("Cookie")
cookie.add_label("Friend")

# call update_name() on cookie
# cookie.update_name(lname="Monster Too")
# cookie.update_name(fname="Yummy Cookie")
# cookie.update_name(fname="Yummy Cookie", lname="Monster Too")
# print(cookie)

# create contact for Don Music
don = Contact("Don", "Music")

# call add_label on don
don.add_label("Music")
don.add_label("Friend")

# call add_phone on don
don.add_phone("12345678", "work")
print(don)

# create contact for Roosevelt Franklin
roosevelt = Contact("Roosevelt", "Franklin")

# call add_email() on roosevelt
roosevelt.add_email("roosevelt@sesame.com")
roosevelt.add_email("frankie@sesame.com")

# call print_emails()
roosevelt.print_emails()

# create a contact book
sesame_street = ContactBook()

# add contacts to contact book
sesame_street.add(cookie)
sesame_street.add(don)
sesame_street.add(roosevelt)

# print the number of contacts in contact book
print(len(sesame_street.contacts))

# print all contacts
sesame_street.print_all_contacts()

# print book
sesame_street.print_book()

# call search_by_label()
sesame_street.search_by_label("Friend")
sesame_street.search_by_label("Music")

# call delete_contact()
sesame_street.delete_contact(roosevelt)
sesame_street.delete_contact(roosevelt)
