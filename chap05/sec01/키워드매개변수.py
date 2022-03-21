def print_n_times(*values, n=2):
    #n번 빈복합니다.
    for i in range(n):
        #values는 리스트 처럼 활용합니다.
        for value in values:
            print(value)
            #단순한 줄바꿈
        print()

#함수를 호출합니다.
print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍", n=5)
