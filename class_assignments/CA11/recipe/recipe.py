# Recipe

list4=[]
list4.append(1)
list4.append(10)
list4.remove(10)

class Recipe:
    list_of_ingredients=[]
    list_of_instructions=[]    
    name=""
    preparation_time=0

    def __init__(self,name,preparation_time):
        # self.ingredients = ["2 avocados", "1 lime", "2 tsp salt"]
        # self.instructions = ["chop avocados", "chop onion",
        #         "squeeze lime", "add salt", "mix well"]

        # print("Welcome....!!!!")
        self.name=name
        self.preparation_time=preparation_time
        pass

  

    def add_ingredient(self, ingredient):
        self.list_of_ingredients=open("ingredients.txt","a+")
        self.list_of_ingredients.writelines(ingredient)
        pass
    def add_instructions(self, instruction):
        self.list_of_instructions=open("instructions.txt","a+")
        self.list_of_instructions.writelines(instruction)
        pass
    def read_ingredients(self):
        self.list_of_ingredients=open("ingredients.txt","r")    
        #print(self.list_of_ingredients.read())
        ingredient=self.list_of_ingredients.readlines()
        for ingredient_ in ingredient:
            print(f"\t * {ingredient_}\n")
        pass

    def read_instructions(self):
        self.list_of_instructions=open("instructions.txt","r") 
        instruction=self.list_of_instructions.readlines()
        for instruction_ in instruction:
            print(f"\t * {instruction_}\n")
        #print(self.list_of_instructions.read())
        pass
    def print_ingredients(self):
        print(f"To make {self.name} you will need:\n")
        print(f"{self.read_ingredients()}")
        
        
    def print_instructions(self):
        print(f"To make {self.name}  you need to do:\n")
        print(f"{self.read_instructions()}")

        pass

# recipe=Recipe("fruite Salat",2)
# recipe.print_ingredients()
# print("\n")
# recipe.print_instructions()