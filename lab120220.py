import numpy as np
# class.function()
#np is the abbrevation for nimpy

#regular list list_name = [1, 2, 3, 4]
list1 = [1, 2, 3, 4]
dir(list1) #prints out functions for list

#to convert a list into a numpy array
np_arr1 = np.array(list1)

print("list: ", list1)
print("numpy: ", np_arr1)


list2d = [[1, 2, 3, 4],
          [2 ,4, 6, 8],
          [3, 6, 9, 12]]
np_2d = np.array(list2d)
print("list: ", list2d)
print("numpy: ", np_2d)

print(np_2d.shape)

np_2d_T = np_2d.T #to get transpose
print(np_2d_T)

vec_ones = np.zeros(10)
print("vec_ones ", vec_ones)

print(np_2d_T[2, 1]) # get value at row 2, column 1
print(np_2d_T[0]) # get everything from row 0
print(np_2d_T[:, 1]) # get everything from column 1


#3e
#np_2d: 3x4
#np_2d_T: 4x3
prod = np.matmol(np_2d, np_2d_T)
print(prod)

#np_2d_T: 4x3
#np_2d: 3x4
prod = np.matmol(np_2d_T, np_2d)
print(prod)

#3f
np1 = np.array([[1, 2], [7, -3]])
print(np1)

inv = np.linalg.inv(np1)
print(inv)
