""" A geometry application needs to calculate the area of rectangles. Create a Rectangle 
class that uses a constructor to initialize length and width. Add a method to calculate 
and display the area.
"""

class Rectangle:
    def __init__(self,l,w):
     self.l = l
     self.w = w

    def area(self):
        print("Area =", self.l*self.w)

r1 = Rectangle(10 ,5)
r1.area()
    



