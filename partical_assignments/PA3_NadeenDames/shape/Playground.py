from Shape import Shape
from Circle import Circle
from Square import Square
from Polygon import Polygon
from Triangle import Triangle

class Playground():
    Circle=Circle(6)
    Polygon=Polygon(3)
    Square=Square(5,2)
    Triangle=Triangle(1,4,2)
    Shape=Shape()
    
    # Implement __init__() for this class

    def __init__(self):
        print("The instances you created")

    # Call Method find_area of each class 

    print(f"{Circle} and area = {Circle.find_area()}")
    print(f"{Square} and area = {Square.find_area()}")
    print(f"{Triangle} and area = {Triangle.find_area()}")

    #find_circumference
    #find_perimeter
    # Call Methods find_circumference and find_perimeter of each class
    print(f"{Circle} and circumference = {Circle.find_circumference()}")
    print(f"{Square} and perimeter = {Square.find_perimeter()}")
    print(f"{Triangle} and perimeter = {Triangle.find_perimeter()}")

    def __str__(self):
        print("Playground...Shapes")
    





