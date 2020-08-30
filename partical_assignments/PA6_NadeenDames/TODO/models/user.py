# Class User

class User:
    def __init__(self, email, password):

        # attibutes
        self.id = id(self)
        self.fname = ""
        self.lname = ""
        self.email = email
        self.password = password
        self.tasklist=list()

    # method to set firstname
    def set_userfirstname(self,fname):
        self.fname=fname

    # method to set lastname
    def set_userlastname(self,lname):
        self.lname=lname

    # method to set email
    def set_useremail(self,email):
        if self.email==" ":
            pass
        else:
            self.email=email

    # method to set password
    def set_userpassword(self,password):
        if self.password== " ":
            pass
        else:
            self.password=password 
        
    # method to add task list
    def add_tasklist(self,tasklist_id):
        self.tasklist.append(tasklist_id)

    # method to get fname
    def get_userfname(self):
        return self.fname
    
    # methos to get lname
    def get_userlname(self):
        return self.lname

     # methos to get email
    def get_useremail(self):
        return self.email

     # methos to get password
    def get_userpassword(self):
        return self.password

    
    