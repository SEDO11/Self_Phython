list_a = [1, 2, 1, 2]
value = 2
run = True


while value in list_a:
    list_a.remove(value)
    
print(list_a)
