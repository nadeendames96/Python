# Class Task
from Priority import Priority
from Status import Status

class Task:

    def __init__(self, title, priority):
        
        # attibutes
        self.id = id(self)
        self.title = title
        self.description = ""
        self.priority = Priority.LOW
        self.status = Status.NOT_STARTED

    # method to set title
    def set_title(self,title):
        if self.title==" ":
            pass
        else:
            self.title=title

    # method to set description
    def set_description(self,description):
            self.description=description

    # method to set priority
    def set_priority(self,priority):
        if self.priority==" ":
            pass
        else:
            self.priority=priority
        
    # method to set status
    def set_status(self,status):
        if self.status==" ":
            pass
        else:
            self.status=status

    # method to get title
    def get_title(self):
        return self.title
    
     
    # method to get description
    def get_description(self):
        return self.description

     
    # method to get priority
    def get_priority(self):
        return self.priority

        
    # method to get status
    def get_status(self):
        return self.status