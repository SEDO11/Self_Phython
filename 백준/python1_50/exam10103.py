#주사위 게임

dice1 = dice2 = 100

run = int(input()) # 라운드 진행 횟수

for i in range(run):
    list_d = input().split()
    a = int(list_d[0]) #창영이
    b = int(list_d[1]) #상덕이
    if a > b: #창영이가 이긴경우
        dice2 -= a # 상덕이 주사위 점수 내림
    elif a < b: #상덕이가 이긴경우
        dice1 -= b # 창영이 주사위 점수 내림

print(dice1) # 창영이 주사위 점수
print(dice2) # 상덕이 주사위 점수