from recipe import Recipe



class Kitchen(Recipe):
    
    recipe=Recipe("fruite salt",2)
    my_recipes=[]
    def __init__(self):
     
      pass
    def favorit_recipe(self,ingredient,instruction):
        self.recipe.add_ingredient(ingredient)
        self.recipe.add_instructions(instruction)
        self.my_recipes.append(self.recipe)
    def print_info(self):
        self.favorit_recipe("2 oranges","add oranges")
        self.recipe.print_ingredients()
        self.recipe.print_instructions()
kitchen=Kitchen()
kitchen.print_info()