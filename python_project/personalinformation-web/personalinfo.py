class PersonalInfo:
    # Constructor 
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        self.email=""
        self.phone=""
        self.dob=""
        self.address=""
        self.educations=list()
        self.experiances=list()
        self.zip=""
        self.school="Roqaia Bent Al-Rasool"
        self.university="Al-Balqa Applied University"
        self.skills=list()

        # Nav bar name

        self.home=""
        self.education=""
        self.experiance=""
        self.skill=""
        self.interest=""
        self.internship=""
        self.certification=""
    
    # Add email for Uuer
    def add_email(self,email):
        self.email=email

    # Add phone for user
    def add_phone(self,phone):
        self.phone=phone

        # Add birthday for user
    def add_bitrhday(self,birthday):
        self.dob=birthday

        # Add education for user
    def add_educations(self,educate):
        self.educations.append(educate)

        # Add experiance for user
    def add_experiance(self,experiance):
        self.experiances.append(experiance)    

        # Add skills for user
    def add_skill(self,skill):
        self.skills.append(skill)    

    # Add address
    def add_address(self,address):
        self.address=address

    #  Add zip code 
    def add_zipcode(self,zip):
        self.zip=zip