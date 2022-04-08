#피보나치 수

n = int(input())
list_a = [0, 1]
for i in range(2, n+1):
    list_a.append(list_a[i-1] + list_a[i-2])
print(list_a[n])