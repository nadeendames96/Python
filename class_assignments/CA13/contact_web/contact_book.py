from contact import Contact

# class ContactBook


class ContactBook:

    # init for ContactBook()

    def __init__(self):

        #
        # instance attributes
        #

        self.contacts = list()

    #
    # instance methods
    #

    # add(contact)
    def add(self, contact):
        self.contacts.append(contact)

    # get_contact(contact, keyword)
    def get_contact(self, contact_id):
        return self.contacts[contact_id]

    # delete_contact(contact)
    def delete_contact(self, contact):
        if contact in self.contacts:
            print("Removing contact...")
            self.contacts.remove(contact)
        else:
            print("Contact does not exist.")

    # get_contacts()
    def get_contacts(self):
        return self.contacts

    # search(keyword)
    def search(self, keyword=""):

        # declare a local variable 'results'
        results = list()

        # loop over every contact in self.contacts
        for contact in self.contacts:

            # call get_contact(contact, keyword)
            contact = self.get_contact(contact, keyword)

            # check if contact exists
            if contact != None:
                # append to list of results
                results.append(contact)

            # check if we found any matches
            if len(results) > 0:
                print(
                    f"Found {len(results)} results matching the keyword '{keyword}'.")
                for contact in results:
                    print(contact)
            else:
                print(f"No results found matching the keyword: '{keyword}'.")

    def search_by_label(self, label):
        print(f"Searching for '{label}'")

        # declare a local variable 'results'
        results = list()

        # loop over every contact in self.contacts
        for contact in self.contacts:
            if contact.check_label(label):
                results.append(contact)

        # check if we found any matches
        if len(results) > 0:
            print(
                f"Found {len(results)} contacts with the label: '{label}'.")
            for contact in results:
                print(contact)
        else:
            print(f"No results found matching the keyword: '{label}'.")

    # print_all_contacts()
    def print_all_contacts(self):
        # print all contacts in contact book
        for contact in self.contacts:
            # print(type(contact))
            print(contact)
            # print(self.contacts)

    # print_book()
    def print_book(self):

        print(f"Printing the book...\n")

        total_number_of_contacts = len(self.contacts)
        contacts_without_phone = 0
        contacts_without_email = 0

        for contact in self.contacts:
            if len(contact.phone_numbers) == 0:
                contacts_without_phone += 1

            if len(contact.emails) == 0:
                contacts_without_email += 1

        print(f"The contact book has {total_number_of_contacts} contacts.")
        print(f"{contacts_without_phone} contacts without a phone number.")
        print(f"{contacts_without_email} contacts without an email address.\n")

        # return contacts_without_phone, contacts_without_email
