# 별찍기 5, n번째 줄에 2*n-1개의 별을 찍자

star = int(input())
for i in range(1, star+1):
    print(" "*(star-i)+"*"*(2*i-1))