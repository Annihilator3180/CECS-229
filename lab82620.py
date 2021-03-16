#

# x = 4
# # y = x / 3 #with decimak
# # z = x // 3 #int division
# y = x % 3 #modus
# z = x ** 3 #to the power of
#
# print(y, z)
#
# if __condition__:
#
#
# if x % 2 == 0:
#     print("even")
# else:
#     print("odd")
#
# x = int(input("Enter a number: "))
#
# if (x < 0):
#     print("Negative")
# elif(x > 0):
#     print("Positive")
# else:
#     print("Zero")

#---------------------------------------

# number = 5
#
# while number > 0: #if using >= the end will need to be -1 since its not inclusive range (5, -1, -1)
#     print(number, end = " ")
#     number -= 1 #number = number - 1
# print()
#
# #for (int i = 0; i > 0; i++)\
# #if you dont include a step size, python will assume its 1
# #for <variable> in range(start, end, step size)
# for number in range(5, 0, 0):
#     print(number, end = " ")
# print()
#
# # python assumes that step size is one
# for i in range(2, 10):
#
# #python assumes that you start is 0 and step size is 1
# for number in range(10):

#-----------------------------
# string = "Traversal"

# for letter in string:
#     print(letter)

# for letter in string:
#     print(letter, end = " ")
#
# for index in range(len(string)): #need range or error will occur
#     print(string[index], end = " ")

# for idx, letter in enumerate(string): #zero to the list of string
#     print(idx, letter)

#exercise assignment
#Given a string, print it out backwards

# str = input("Enter a str: ")
# str_len = len(str)
#
# for index in range(str_len - 1 , -1, -1):
#     char = str[index]
#     print(char, end="")

#------------------------------
#lists

# listOfItems = [1, "one", 1.1]
# listOfLists = [listOfItems, [1, 2]]
#
# for item in listOfItems:
#     print(item, end=" ")
#
# print()
#
# #adding an item
# listOfItems.append("two")
#
# for item in listOfItems:
#     print(item, end=" ")
#
# print()
# listOfItems.pop()
#
# for item in listOfItems:
#     print(item, end=" ")
#
# print()
# listOfItems.pop(0)
#
# for item in listOfItems:
#     print(item, end=" ")
#
# print()

#append(), pop()

#------------------------------------------------------------
#list.append(thing)
#adds thing to the end of the list

# L1 = [1, 2, 3, 4, 5, 6, 7, 6]
#
# #do NOT do this
# #NOT A COPY. L2 is referencing, shallow copy
# # L2 = L1
# #instead use
# L2 = L1.copy()
#
# #list.insert(index, thing)
# #insert thing to index __
# # at index 3, insert 4
# L1.insert(3, 4)
# print(L1)
#
# #list.remove(thing)
# #removes thing from list
# L1.remove(6)
# print("L1", L1)
# print("L2", L2)

# # to see whats in array

# if 8 in L1:
#     print("is in the list")
# else:
#     print("is not in list")

print("Hello world")


