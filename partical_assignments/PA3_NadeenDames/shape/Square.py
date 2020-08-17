from Polygon import Polygon

# Square class


class Square(Polygon):
    def __init__(self, length, width):
        super().__init__(2)
        self.length = length
        self.width = width

    def find_area(self):
        return self.length * self.width

    def find_perimeter(self):
        return 2 * self.length + 2 * self.width
    
    def __str__(self):
        return f"I am a square with {self.length} length and {self.width} width"
    def print_information(self):
        print(f"The area of this square is {self.find_area()} and perimeter of this square  is {self.find_perimeter()}")
    def draw_shape(self,Shape): 
        print(f"{Shape} is drawing...")