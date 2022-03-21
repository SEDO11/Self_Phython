def call_10_times(func): #여기에 print_hello가 이동
    for i in range(10):
        func() #여기에서 print_hello로 바뀌면서 해당 함수 실행
        
def print_hello():
    print("안녕하세요")
    
call_10_times(print_hello)