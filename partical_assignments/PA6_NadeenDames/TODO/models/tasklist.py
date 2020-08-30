# Class TaskList

class TaskList:

    def __init__(self):

        # attibutes
        self.id = id(self)
        self.tasklistname ="Personality List"
        self.tasks_id = list()
        self.taskslist=list()
        self.description="personality list"
        self.avator="https://www.iconspng.com/images/task/task.jpg"
    # method to set task list title
    def set_tasklistname(self,tasklistname):
             self.tasklistname=tasklistname
    # method to get task list 
    def get_tasklistname(self):
        return self.tasklistname
    
    # method to update avator 
    def update_avator(self,avator):
        self.avator=avator
    
    # method to get tasklists
    def gettaskslist(self):
        return self.taskslist

    # method to set decription
    def set_description(self,description):
        self.description=description

    # method to get description
    def get_description(self):
        return self.description

def generate_tasklist_info():
     tasklist=TaskList()
     return tasklist
    