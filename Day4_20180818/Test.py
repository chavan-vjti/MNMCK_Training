# def square_n():
# 	n = [i for i in range(1,31)]
# 	sq_n = list(map(lambda x: x**2, n))
# 	return sq_n
# print(square_n())

# Adds all the number with decrement


# def recursion(n):
#     if n ==1:
#         return 1
#     else:
#         add = n + recursion(n-1)
#     return add
#
#
# p = int(input("Enter a number: "))
# print(recursion(p))

# n=int(input("Enter number of rows: "))
# a=[]
# for i in range(n):
#     a.append([])
#     a[i].append(1)
#     for j in range(1,i):
#         a[i].append(a[i-1][j-1]+a[i-1][j])
#     if(n!=0):
#         a[i].append(1)
# for i in range(n):
#     print("   "*(n-i),end=" ",sep=" ")
#     for j in range(0,i+1):
#         print('{0:6}'.format(a[i][j]),end=" ",sep=" ")
#     print()

# class power_n():
#     def __init__(self, num, power):
#         self.num = num
#         self.power = power
#
#     def powernum(self):
#         return self.num ** self.power
#
# c1 = power_n(2,3)
# # print(c1.power_num())
# print(c1.powernum())

# class Demo():
#     def __init__(self):
#         self.astring = ""
#
#
#     def get_string(self):
#         self.astring = input("Enter a string: ")
#
#     def print_string(self):
#         self.astring = self.astring.upper()
#         print("Entered string is %s" % self.astring)
#
#
# b1 = Demo()
# b1.get_string()
# b1.print_string()

# import itertools
# class uniqe_subsets():
#     def __init__(self):
#         self.b = ""
#
#     def get_numb(self):
#         a = input('Enter integers space separated: ')
#         self.b = [int(x) for x in a.split(' ')]
#
#     def comination(self):
#         for i in range(0, len(self.b)+1):
#             for combi in itertools.combinations(self.b, i):
#                 if not combi == None:
#                     print(combi, end='')
#
# obj1 = uniqe_subsets()
# obj1.get_numb()
# obj1.comination()

# import itertools
#
#
# class specific_sum():
#     def __init__(self):
#         self.a = ""
#
#     def get_array(self):
#         b = input('Enter an array, space separated: ')
#         self.a = [int(x) for x in b.split(' ')]
#
#     def get_numb(self):
#         c = int(input("Enter a target number: "))
#         temp_list = []
#         for i in itertools.combinations(self.a, 2):
#             if i[0] + i[1] == c:
#                 temp_list.append(i)
#                 print(i)
# obj2 = specific_sum()
# obj2.get_array()
# obj2.get_numb()

# import itertools
#
# class sum_to_zero():
#     def __init__(self):
#         self.a = ""
#
#     def get_number(self):
#         b = input('Enter an array, space separated: ')
#         self.a = [int(x) for x in b.split(' ')]
#         for i in range(len(self.a)):
#             for j in itertools.combinations(self.a, 3):
#                 if j[0] + j[1] + j[2] == 0:
#                     print(j)
# obj3 = sum_to_zero()
# obj3.get_number()

import numpy as np
# arr1 = np.array([1.2,-2.4,3,4])
# arr1_rev = np.empty(arr1.shape)
# # np.set_printoptions(suppress=True)
# for index, i in enumerate(arr1):
#     index+=1
#     arr1_rev[-index] = i
#     print(arr1_rev)

# arr3 = np.zeros((6,6))
# arr3[0] = np.ones(arr3.shape[1])
# arr3[-1] = np.ones(arr3.shape[1])
# i = 1
# while i < (arr3.shape[1]-1):
#     arr3[i][0] = 1
#     arr3[i][-1] = 1
#     i += 1

# p = int(input("Enter the square order of matrix: "))
arr = np.ones((8,8), dtype='int32')
arr[::2,::2] = 0
arr[1::2,1::2] = 0
print(arr)
# arr1 = np.arange(1, 10).reshape((3, 3))
# arr2 = np.zeros((3,3))
# arr3 = arr1 + arr2