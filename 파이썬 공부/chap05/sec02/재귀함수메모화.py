memo = {
    1: 1,
    2: 1
}
# 1, 2 는 있으니 계산 안하고 딕셔너리에 저장,
# 그 다음 부터는 계산 후 저장한다.
counter = 0
def f(n):
    global counter
    counter += 1
    if n in memo:
        print("메모에 값이 있으면 가져옴 counter:", counter, memo.keys())
        return memo[n] #조기 리턴, 이걸 사용하는게 더 좋음
    output = f(n-1) + f(n-2)
    memo[n] = output # 딕셔너리에 값 넣고
    print("메모에 값이 없으면 계산후 저장 counter:", counter, memo.keys())
    return output # 출력
    
print(f(10)) # f(10) * f(9) * f(8) ... * f(0)
print(counter)
# for i in memo:
#     print(i)