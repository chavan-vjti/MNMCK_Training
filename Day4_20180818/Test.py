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

class Demo():
    def __init__(self):
        self.astring = ""


    def get_string(self):
        self.astring = input("Enter a string: ")

    def print_string(self):
        self.astring = self.astring.upper()
        print("Entered string is %s" % self.astring)


b1 = Demo()
b1.get_string()
b1.print_string()
