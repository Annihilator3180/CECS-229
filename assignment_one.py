

"""question 1"""

# def euclid_algo(x, y, z=True):
#     if x < y:
#         return euclid_algo(y, x, z)
#     print()
#     while y != 0:
#         if z:
#             print('%s = %s * %s + %s' % (x, x // y, y, x % y))
#         (x, y) = (y, x % y)
#
#     if z:
#         print('gcd is %s' % x)
#     return x
#
# euclid_algo(150, 304)
# euclid_algo(1000, 10)
# euclid_algo(150, 9)

"""answer"""
# a = 512
# b = 3
#
# x = a
# y = b
# while y != 0:
#     r = x % y
#
#     x = y
#     y = r
#

"""question 2"""
# def validate(userinput: str):
#     #Check if the given str is a binary string (containing '0' and '1' only)
#     for char in userinput:
#         if not (char == '0' or char == '1'):
#             return False
#     return True
#
# def convert(userinput: str):
#     #Convert the binary string into its equivalent decimal
#     value = 0  # Accumulate from each bit
#
#     for i in range(len(userinput)):  # bitIdx = 0, 1, 2, ..., len()-1
#         bit = userinput[i]
#         if bit == '1':
#             value += 2 ** (len(userinput) - 1 - i)  # ** for power
#     return value
#
# def main():
#     """The main function"""
#     userinput = input('Enter binary number: ')
#     if not validate(userinput):
#         print('Error, invalid binary number "{}"'.format(userinput))
#     else:
#         print('The decimal number for binary "{}" is: {}'.format(userinput, convert(userinput)))
#
# if __name__ == '__main__':
#     main()


"""answer"""
# bin_string = "101"
#
# l = len(bin_string)
# dec_num = 0
#
# for i int range(l):
#     digit = int(bin_stirng[l-i-1])
#     dec_num += digit * 2 ** i
#
# print(bin_string, "as a decimal number:", dec_num)

"""question 3"""

# class Rectangle:
#
#     def __init__(self, w = 1, h = 1):
#         self.width = w
#         self.height = h
#
#     def getArea(self):
#         return self.width * self.height
#
#     def getPerimeter(self):
#         return 2 * (self.width + self.height)
#
# w = 4
# print('The width of rectangle is: '+ str(w))
# h = 40
# print("The height of rectangle is: " + str(h) + "\n")
# #Call method by passing the width and height.
# r = Rectangle(w,h);
#
# #Print area and perimeter.
# print("The area of the rectangle is", r.getArea());
# print("The perimeter of the rectangle is", r.getPerimeter());
# print("")
# w = 3.5
# print("The width of the rectangle is "+str(w))
# h = 35.9
# print("The height of the rectangle is "+str(h) + "\n")
#
# #Call method by passing the width and height.
# r = Rectangle(w,h);
#
# #Print the area and perimeter.
#
# print("The area of the rectangle is", r.getArea()) ;
# print("The perimeter of the rectangle is", r.getPerimeter());


