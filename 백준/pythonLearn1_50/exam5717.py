# 상근이의 친구들

while True:
    list_a = input().split()
    a = int(list_a[0])
    b = int(list_a[1])
    
    if a==0 and b==0:
        break
    result = a + b
    print(result)