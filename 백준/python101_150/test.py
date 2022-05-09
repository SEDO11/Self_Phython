# li = ['Korea', 'America', 'China']
# a=0
# str01 = ""
# # 파이썬에서 for문은 다른 언어의 foreach 문 처럼 동작
# # 여기서는 3번 왜냐하면 li가 Korea, America, China 이렇게 3개의 값을 갖기 때문
# for i in li: #i에 korea, America, China가 들어옴
    
#     #여기에서는 Korea, 5글자, 5번 반복 / America, 7글자, 7번 반복 / China 5글자, 5번 반복
#     for j in i: # j에 i 내부의 글자가 하나씩 들어감
#         str01 += j # 1.K 2.o 3.r 4.e 5.a
#         print(j)
        
#         # 근데 여기에서 a가 5 이상, 즉 5번 이상 실행 됐다면 멈추라고 명령 했으므로
#         # Korea에서 이미 5번 반복 했기에 뒤에 America나 China는 앞에 한 글자만 입력되고 종료
#         a = a + 1
#         if a > 6:
#             break
# print('a :', a, ', str01 :', str01)

def soojebi(num):
    print(num%2)
    if num < 2:
        print(num)
    else:
        soojebi(num//2)
        print(num%2)
soojebi(20)