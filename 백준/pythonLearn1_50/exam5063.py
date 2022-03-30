#TGN

run = int(input()) #실행 횟수 입력

for i in range(run): 
    rec = input().split()
    r = int(rec[0]) # 광고를 하지 않았을 때 수익
    e = int(rec[1]) # 광고를 했을 때 수익
    c = int(rec[2]) # 광고 비용
    
    if r + c < e: # 광고를 했을 때 더 이득인 경우
        print("advertise")
    elif r + c == e: # 하거나 안하거나 똑같은 경우
        print("does not matter")
    else : # 광고를 안했을 때 더 이득인 경우
        print("do not advertise")
