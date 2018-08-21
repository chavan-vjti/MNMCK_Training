# def square_n():
# 	n = [i for i in range(1,31)]
# 	sq_n = list(map(lambda x: x**2, n))
# 	return sq_n
# print(square_n())

# Adds all the number with decrement


def recursion(n):
    if n ==1:
        return 1
    else:
        add = n + recursion(n-1)
    return add


p = int(input("Enter a number: "))
print(recursion(p))
