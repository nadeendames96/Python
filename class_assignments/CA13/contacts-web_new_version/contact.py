# Class Contact

class Contact:

    # init for Contact(fname, lname)
    def __init__(self, fname, lname):

        #
        # instance attributes
        #
        self.friends=list()
        self.likes=list()
        self.birthday="1/1/1969"
        self.address="Jordan"
        self.id = id(self)
        self.fname = fname
        self.lname = lname
        self.emails = list()
        self.phone_numbers = dict()
        self.labels = list()
        self.avatar_url = "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fimages.wikia.com%2Fmuppet%2Fimages%2Fa%2Faa%2FCookieMonsterOpenedMouth.png&f=1&nofb=1"
        # self.biography="Welcome my profile,not have any information about me"    
        print(f"A new contact for '{self.fname}' has been created.")

    #
    # instance methods
    #

    # override __str__()
    def __str__(self):
        # override __str__
        return f"""
        Contact information for {self.lname.capitalize()}, {self.fname.capitalize()}.
        Contact has {len(self.phone_numbers)} phone numbers and {len(self.labels)} labels.
        """

    # add_phone(phone_number, label)
    def add_phone(self, phone_number, label):

        # check if this is the first number added
        if len(self.phone_numbers) == 0:
            label = "primary"

        # add the phone_number to the contact list of phone numbers
        self.phone_numbers[label.lower()] = phone_number

    # add_label(label)
    def add_label(self, label):
        # append label to the contact list of labels
        self.labels.append(label)
     # add_likes   
    def add_likes(self,like):
        self.likes.append(like)

    # add_friends   
    def add_friends(self,friend):
       self.friends.append(friend.id)   
    
    #  get friends
    def get_friends(self):
        return self.friends

    # add_email(label)
    def add_email(self, email):
        self.emails.append(email)
    # update_address
    def update_address(self,address):
        self.address=address
    def update_birthday(self,birthday):
        self.birthday=birthday
    # update_biography(biography)
    def update_biography(self, biography):
        self.biography = biography

    # update_name(fname, lname)
    def update_name(self, fname="", lname=""):
        if fname != "":
            self.fname = fname

        if lname != "":
            self.lname = lname

    # check_label()
    def check_label(self, label):
        if label in self.labels:
            return True
        else:
            return False

    # print emails()
    def print_emails(self):
        for email in self.emails:
            print(f"{self.fname} has email: '{email}'")
    def delete_phone(self,phone_key):
     del self.phone_numbers[phone_key]
    def get_name(self):
        return self.fname