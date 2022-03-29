#최소공배수

run = int(input()) # 입력 개수
result = 0

def gcd(a, b): # 최대 공약수 알고리즘
    while b != 0:
        r = a%b
        a=b
        b=r
    return a

for i in range(run):
    list_a = input().split() # 공백으로 나눔
    a = int(list_a[0])
    b = int(list_a[1])
    c = gcd(a, b)
    result = (a * b) // c # 최대 공배수 구하는 공식
    print(result)