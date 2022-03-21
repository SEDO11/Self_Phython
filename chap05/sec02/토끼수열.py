def rabbit(n):
    result = 0
    if n == 1:
        return 1
    elif n == 1:
        return 1
    else:
        return rabbit(n-1) + rabbit(n -2)
    
# print(rabbit(1))
# print(rabbit(2))
print(rabbit(3))
# print(rabbit(4))
# print(rabbit(5))