# #Python Dictionary
# #It's equivalent to a Java/C++ HashMap
# #{key1: value1, key2 : value2...}
# #How to make a dictionary
# """
# In [1]:       #if you know key/value combos
#               dict1 = {"red" : "Twizzlers", "orange" : "starburst", "yellow" : "lemonheads",
#                        "green" : "juicy drop pops"}
#
#               #to make and empty dictionary
#               dict2 = {} #this can get confusing because sets go in {}
#               dict3 = dict{}
#
#               #data structures
#               #list []
#               #tuples ()
#               #dictionaries {}
#               #sets {}
# """
# ##Acessing values in dictionary
# #dict_name[key]
# """
# In [2]: print(dict1["red"])
# #returns Twizzlers
#
# print(dict1["purple"])
# #returns a KeyError = that key does not exist in dictionary
# """
#
# ##Adding things into dictionary
# """
# dict_name[new_key] = new_value
#
# In [5] : "chocolate"
# print(dict1)
#
# {"red" : "Twizzlers", "orange" : "starburst", "yellow" : "lemonheads",
#                        "green" : "juicy drop pops", 'brown': 'chocolate'}
# """
#
# ##Looping through a dictionary
# """
# for each key in the dictionary...
#
# In []:
# """
# #the variable used in the for loop represents the KEY only
# """
# for color in dict:
#         print(color, dict1[color])
# #returns these values
# # red Twizzlers
# # orange starburst
# # yellow lemonheads
# # .
# # .
# # .
# """
# # using dict_name.values() will allow direct access to the values instead of the key
# """
# for candy in dict.values():
#     print(candy)
# # returns these values
# # Twizzlers
# # starburst
# # lemonheads
# # juciy drop pops
# # chocolate
#
# """
# #------------------------------------------------------------------------------------------------
# #Making our own vector class
#
# In [1]:
# class Vector:
#     # labels is like your domain (a set)
#     # function is your function
#     def __init__(self, labels, function):
#         self.D = labels
#         self.fun = function
#
#
# In[7]:
# v1 = Vector({'x', 'y', 'z'}, {'x': 1, 'y': -3})
# for d in v1.D: #goes thru
#     if d in v1.fun:
#         print(v1.fun[d])
# #1
# #-3
#
# #setter/mutator: add in (d:val) into your vec
# ##Getters and setters for our vectors
# #vec vector taht we want to alter
# #d: new key for vec's fun
# #val: new value fopr vec's fun
# In[6]:
# def setitem(vec, d, val):
#     #add combo d:val into vec's fun
#     vec.fun[d] = val
#
# #getter/accessor: get the value of d from your vec
# #vec: vector that you want to access data from
# #d: element you want to get the value of
# def getitem(vec, d):
#     #if the key that we are checking is NOT in the domain,
#     #then we return None
#     if not d in vec.D:
#         return None
#     elif d in vec.fun:
#         return vec.fun[d]
#     #if the key that we are checking is part of the domain but has no value in dictionary
#     #then tje value wi;; default to 0
#     else:
#         return 0
#
#
#
#
# setitem(v1, 'z', 3.6)
#
#
# #printing vector again
# for d in v1.D: #goes thru
#     if d in v1.fun:
#         print(d, v1.fun[d])
#
# # x 1
# # y -3
# # z 3.6
#
# print("value of x:", getitem(v1, 'x'))
# print("value of a:", getitem(v1, 'a'))
#
# #value of x: 1
# #value of a: None
#
# ##Scalar multiplication
#
# u = [1,2,3]
# 2u = [2,4,6]
#
# In[]:
#
# #distribute the scalar (alpha) to the vector (vec)
# def scalar_mul(vec, alpha):
#     #for every key in vec's fun in dictionary
#     for key in vec.fun:
#         #vec dictionary
#         vec.fun[key] *= alpha
#         #vec.fun[key] = vec.fun[key] * alpha
#
# scalar_mul = (v1, -2)
#
# for d in v1.D: #goes thru
#     if d in v1.fun:
#         print(d, v1.fun[d])
#
# #x -2
# #y 6
# #z -7.2
#
#
# ##Vector Addition
# #[1, 2, 3] + [-5, 8, 0] = [-4, 10, 3]
#
# In[]:
# #Two vectors as inputs so we can add them
# #this needs to return a new vector (sum)
#
# def vec_addition(vec1, vec2):
#     #loop thru domain of the first vector and check if it is in the second vector
#     for d in vec1.d:
#         #if an element of vec1's domain is NOT in vec2's domain, then we cannot add
#         #the two vectors and we just return None
#         if not d in vec2.d:
#             return None
#     #if we are done checking and it has not returned None yet
#     #then add the two vectors
#     temp_dict = {}
#     for d in vec1.d:
#         #adds the two items together and stores it in our temp dictionary
#         temp_dict[d] = getitem(vec1, d) + getitem(vec2, d)
#     #returns a new vector with same domain as vec1 or vec2 and with new dictionary of sums
#     return Vector(vec1.Domain, temp_dict)
#
# v2 = Vector({'x', 'y', 'z'}, {'x': 1, 'y': 2, 'z': 3})
# #v1 = [-2, 6 ,-7.2]
# #v2 = [1, 2, 3]
# v3 = vec_addition(v1,v2)
#
# for d in v3.Domain:
#     if d in v3.fun:
#         print(d, v3.fun[d])
#
# #z -4.2
# #y 8
# #x -1