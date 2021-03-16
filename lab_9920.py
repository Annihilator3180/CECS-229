## classes.py
"""
# #def functionName(arguments):
# def compute(x, y): ##arguments are ur variables
#     if x > y:
#         return x
#     elif x < y:
#         return y
#     else:
#         return "equal"
#
#
# test1 = compute(1, 3)
# print(test1, type(test1))
#
# test2 = compute(4, 6.27)
# print(test2, type(test2))
#
#
# test3 = compute(1,1)
# print(test3, type(test3))
"""

#_____________________________________________________

"""
# to create a class: class <classname>
class Dog:

    # constructor
    #_ _ init _ _ (
    # def __init__(self, agruments):
    # if you want multiple constructors, you can
    # predefine optional attributes
    # predefined attributes should be at the end
    def __init__(self, name, age = 0):
        # self.name is not then same as name
        # self.name is a class attribute
        # name is just a local variable
        self.name = name
        self.age = age

    # woof if it is under 2 yrs old
    # bark if it is 2 or over
    def speak(self):
        if self.age < 2:
            print("Woof")
        else:
            print("Bark")

    # increment the age
    def birthday(self):
        self.age += 1 #dont put age += 1

    #accessor/getter
    def getName(self):
        return self.name



    #toString (need this to print out actual thing, not address
    # include self whenever function needs to refer to
    # class attributes or functions
    def __str__(self): ##need self variable to pass argument
        string = "Name: " + self.name
        string += "\nAge: " + str(self.age)
        return string

d1 = Dog("Spot", 4)
d1.speak()
print(d1.getName())
print(d1, "\n") #returns the memory address if there is no toString


d2 = Dog("Kevin")
d2.speak()
print(d2) #will give error since no age argument, add age = 0 ti args in __init__\print(d2)
d2.birthday()
print(d2)
"""
#------------------------------------------------

