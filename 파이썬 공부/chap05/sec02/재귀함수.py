# 재귀함수, 함수를 이용해 해당 조건이 끝날 때 까지 실행
def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)

print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))
print("4!:", factorial(4))
print("5!:", factorial(5))