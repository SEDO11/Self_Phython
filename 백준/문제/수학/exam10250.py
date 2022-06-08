#호텔
# 변수를 floor랑 num로 선언 안하면 백준에서 에러 뜸 ㄷㄷ
t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    num = n // h + 1
    floor = n % h
    if floor == 0: # 호수가 0인 경우
        num = n // h
        floor = h
    print(f'{floor*100+num}')
    # print("{}0{}".format(floor, num)) 이 것도 에러 뜸