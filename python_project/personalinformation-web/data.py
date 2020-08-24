from personalinfo import PersonalInfo

def generate_data():
    # Add Personal Information , Firstname,Lastname,Email,Phone,Educations,Experiance,Skills,Birthday,Address,Zip Codes
    
    # Add Firstname && Lastname
    personalinfo=PersonalInfo("Nadeen","Dames")

    # Add Educations
    personalinfo.add_educations("Elementry School (Scientific section)")
    personalinfo.add_educations("Bechlors (Software Engineering major - GPA : 3.00)")

    # Add Experiance
    personalinfo.add_experiance("Trainee of  Jamal49 | Beloyed Soluations")
    personalinfo.add_experiance("Junior Android Developer     [1 year] EXP") 
    personalinfo.add_experiance("Devloper I'm still a trainee") 
    personalinfo.add_experiance("Java skills [2 years] EXP") 
    personalinfo.add_experiance("Firebase database") 
    personalinfo.add_experiance("SQL database ") 

    # Add Skills
    personalinfo.add_skill("Organizational and planning skills.")
    personalinfo.add_skill("Reliable, with decision making oriented mindset.")
    personalinfo.add_skill("Excellent verbal and written communication skills both within office environment and with external stakeholders.")
    personalinfo.add_skill("Experienced in giving presentations to large audiences.")

    personalinfo.home="home"
    personalinfo.education="education"
    personalinfo.experiance="experiance"
    personalinfo.interest="interest"
    personalinfo.internship="internship"
    personalinfo.skill="skill"
    personalinfo.certification="certification & awards"
    
    return personalinfo
