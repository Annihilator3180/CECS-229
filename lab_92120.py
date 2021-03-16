# x = 1.
# x = int(x)
# print(type(x))
# y = 4.3
# y = int(y)
# print(type(y), y)
#
# z = 23
# z = int(z) #if u hash this out, you will get error(datatype)
# print(type(z), z + 1)

# a = 1234
# a = str(a)
# a += 5
# a = int(a)
# print(a + 10)

#use the datatype names to convert between datatypes
# int(), str(), float(), list()

# m = 10
# n = 3
#
# print("+", m + n)
# print("-", m - n)
# print("*", m * n)
# ## / is true division
# print("/", m / n)
# ##// floor division
# print("//", m // n)
# #** is power m^n
# print("**", m ** n)
# print("%", m % n)

# class Car:
#     #making  to make a constructor __init__(arguments)
#     def __init__(self, color, year, mileage = 0):
#         # if no mileage is passed thru the constructior, set it to zero
#         self.color = color #local var to use for contructor and wont be used for anywhere else
#         self.mileage = mileage
#         self.year = year
#
#     # mileage should increase by m
#     def increase_mileage(self,m):
#         self.mileage += m #self.mileage = self.mileage + m
#
#
#     # accessor: get color
#     def get_color(self):
#         return self.color
#
#     # toString()
#     def __str__(self):
#         string = "color: " + self.color #or self.getcolor()
#         string += "\nmileage: " + str(self.mileage)
#         string += "\nyear: " + str(self.year) #need self to distinguish from car
#         return string
#
# # c1 = Car("black", 2000, 2019)
# # print(c1) prints out mem address
#
# c1 = Car("black", 2019, 20000)
# print(c1, "\n")
#
# c2 = Car("white", 2020)
# print(c2, "\n")
# c2.increase_mileage(150)
# print(c2, "\n")
# print(c2.get_color())
