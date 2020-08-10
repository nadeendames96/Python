from Shape import Shape

# Circle class


class Circle(Shape):
    pass
    # TODO: Implement __init__() for this class

    def __init__(self, radius=1.0):
        # Implemention  __init__ from Shape Class
        super().__init__()
        # Remember this is a subclass of Shape!
        self.radius = radius

    # TODO: Implement find_area() for this class
    def find_area(self):
        return 3.14 * self.radius**2

    # TODO: Implement find_circumference() for this class
    def find_circumference(self):
        return 2 * 3.14 * self.radius
    def __str__(self):
        return f"I am a circle Shape with {self.radius} radius"
    def print_information(self):
        print(f"The area of this circle is {self.find_area()} and circumference of this circle  is {self.find_circumference()}")
    def draw_shape(self,Shape): 
        print(f"{Shape} is drawing...")