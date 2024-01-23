

class Rectangle():
    def __init__(self):
        self.length = 1 
        self.width = 1
    
    def perimeter(self):
        return self.length*2 + self.width*2
    
    def area(self):
        return self.length*self.width



rect = Rectangle()

rect.length
rect.width
rect.perimeter()
rect.area()

rect.length = 4
rect.width = 2

rect.perimeter()
rect.area()

