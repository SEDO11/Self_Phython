def print_n_times(value, n=2): #n에 기본 값을 선언해줌
    # n번 반복합니다.
    for i in range(n):
        print(value)
        
# 함수를 호출
# 기본 매개변수에 값을 안 넣었을 때
print_n_times("안녕하세요")
print()
# 기본 매개변수에 값을 넣었을 때
print_n_times("안녕하세요", 5) #기본매개변수에 값을 넣어주면 해당 값으로 변환됨