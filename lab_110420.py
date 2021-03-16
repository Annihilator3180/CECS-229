#operator overloading


class Point:
    # constructor
    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y

    #we overloaded the __str__ operator
    #to String
    #overrides the original function which prints the address
    #we provide our own string that we want to see printed
    def __str__(self):
        string = "(" + str(self.x) + "," + str(self.y) + ")"
        return string

    """OPERATOR OVERLOADING"""
    #self + other
    #adds x and y coordinates of self and other
    #then returns a nnew point with those coordinates
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x, y)




p1 = Point(1, 7)
#print(p1)
p2 = Point(-3, -9)
#here p1 is self and p2 is other
p3 = p1 + p2
p4 = p1 - p2

print(p4)
print(p3) #Ideally we want to see (-2, -2)
#TypeError: unsupported operand type(s) for +: 'Point' and 'Point'
#Python doesn't know how to add these 2 objects together
#You must use operator overloading to define the operation
