# """question 1"""
# import random
#
# #define the function gcd
# def gcd(a,b):
#     if b==0:
#         return a
#     else:
#         return gcd(b,a%b)
#
# def main():
#     #taking the user inputs
#     p = random.randint(100, 1000)
#     q = random.randint(100, 1000)
#     n = p*q
#     t = (p-1)*(q-1)
#
#     for e in range(2,t):
#         if gcd(e,t)== 1:
#             break
#
#     #print the output
#     print('e = ' + str(e) + ', n = ' + str(n))
#     # print("p =", p)
#     # print("q =", q)
#
# if __name__=='__main__':
#     main()

#-----------------------------------------------------------
"""question 2"""

# def SieveOfEratosthenes(n):
#
#   prime = [True for i in range(n + 1)]
#   p = 2
#
#   while (p * p <= n):
#
#     if (prime[p] == True):
#       for i in range(p * 2, n + 1, p):
#         prime[i] = False
#     p += 1
#   prime[0]= False
#   prime[1]= False
#   for p in range(n + 1):
#     if prime[p]:
#       print(p, end = " ")
#
# # main
# if __name__=='__main__':
#   n = int(input("Enter the value of n: "))
#   print("Prime numbers of %d are: " %n)
#   SieveOfEratosthenes(n)

#----------------------------------------------------------
"""question 3"""

# def multiplyList(myList):
#     # Multiply elements one by one
#     result = 1
#     for x in myList:
#         result = result * x
#     return result
#
# def get_divisors(result):
#     i = 1
#     while i <= result:
#         if (result % i == 0):
#             print(i, end= ' ')
#         i = i + 1
#
# def main():
#     list1 = [2, 2, 3, 3] #36
#     print("The divisors from" , multiplyList(list1))
#     get_divisors(multiplyList(list1))
#
#     print(" \n ")
#     list2 = [3, 2, 4] #24
#     print("The divisors from" , multiplyList(list2))
#     get_divisors(multiplyList(list2))
#
#     print("\n")
#     list3 = [2, 3, 5]
#     print("The divisors from", multiplyList(list3))
#     get_divisors(multiplyList(list3))
#
# if __name__=='__main__':
#     main()
