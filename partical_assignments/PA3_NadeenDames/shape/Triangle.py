from Polygon import Polygon

# Triangle class


class Triangle(Polygon):
    
    # TODO: Implement __init__ for this class
    def __init__(self,base,hight,length):
        # Remember this is a subclass of Polygon!
        super().__init__(3)
        #self.base=base
        self.hight=hight
        self.length=length
        self.base=base
        

    # TODO: Implement find_area() for this class
    def find_area(self):
        return (0.5*self.base*self.hight)
        

    # TODO: Implement find_perimeter() for this class
    def find_perimeter(self):
        return 3*self.length
    def __str__(self):
        return f"I am a triangle with {self.length} length and {self.hight} hight"
    def print_information(self):
        print(f"The area of this triangle is {self.find_area()} and perimeter of this triangle  is {self.find_perimeter()}")

    def draw_shape(self,Shape): 
        print(f"{Shape} is drawing...")