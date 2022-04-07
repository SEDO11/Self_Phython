#별 찍기 20
# " "*입력된 크기 - i(loop) + "*"로 시작
# 뒤는 " *"로 출력되게 하여 이어 붙임
n = int(input())
for i in range(1, n+1):
    print(" "*(n-i)+"*"+" *"*(i-1))