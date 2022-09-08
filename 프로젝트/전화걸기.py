# 전화 걸기 프로그램

# 키: 전화번호 / 값: 이름
dic = {'10' : '이현우', '82' : '손준혁', '20' : '김태현', '30' : '최준혁', 
       '62' : '이준희', '40' : '배성준', '50' : '김중옥', '22' : '김찬영', 
       '70' : '이종호', '12' : '김준성', '80' : '김성빈', '32' : '유지현',
       '42' : '백주호', '60' : '신준철', '52' : '석진욱', '72' : '정명식'} # 각자의 이름과 전화번호를 키, 값 형태로 딕셔너리를 통해 저장

def call(): # 통화 한 후 선택
    print('\n상대방이 먼저 전호를 끊을 경우!!! -1\n당신이 먼저 전화를 끊을 경우!!! -2\n강제 복구인 경우 -3\n상대방이 통화 중 시험인 경우 -4')
    while True:
        n = int(input())
        if n == 1:
            print('상대방이 전화를 끊었습니다.')
            break
        elif n == 2:
            print('당신이 전화를 끊었습니다.')
            break
        elif n == 3:
            print('강제 복구 됬습니다.')
            break
        elif n == 4:
            print('상대방이 통화 중입니다.')
            break
        else:
            print('번호를 잘 못 눌렀습니다.')

def select(): # 통화 선택
    print('\n통화를 원하면 원하는 경우(응답) -1\n통화를 원하지 않는 경우(회의 중) -2\n상대방이 응답을 하지 않는 경우 -3\n발신가입자가 전화를 끊는 경우 -4')
    while True:
        n = int(input())
        if n == 1:
            print('상대방과 응답이 되었습니다.')
            call()
            break
        elif n == 2:
            print('당신이 통화를 거절하였습니다.')
            break
        elif n == 3:
            print('상대방이 응답하지 않습니다.')
            break
        elif n == 4:
            print('상대방은 지금 전화를 받을 수 없습니다.')
            break
        else:
            print('번호를 잘 못 눌렀습니다.')

def ring(m, y): # 호출
    print(dic.get(m), '(이)가', dic.get(y), '에게 전화를 겁니다.')
    print(dic.get(y), '(이)가 R.B.T(호출음)을 받고있는 상태!',  dic.get(y), '(이)가 호출신호(Ring)를 받음')
    select()

while True:
    print('\n전화 번호 부: ', dic, '\n')
    print('자신의 전화번호를 입력하세요 "0을 입력할 경우 종료">', end="")
    m = input()
    if m == '0':
        print('통화를 종료합니다.')
        break
    print('상대방의 전화번호를 입력하세요 >', end="")
    y = input()
    if m in dic and y in dic:
        if m == y:
            print('상대방의 전화번호가 잘못 되었습니다.')
        if m != y:
            ring(m, y)
    else:
        print('없는 번호 입니다.\n')