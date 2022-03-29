#과자

list_abc = input().split()
a = int(list_abc[0])
b = int(list_abc[1])
c = int(list_abc[2])

mom = a * b - c # 어머니 한테 받을 돈 계산
if mom <= 0: # 음수거나 0일 경우, 현재 갖고 있는 돈이 내가 살 것보다 많으므로
    mom = 0 # 어머니 한테 받을 돈 없으므로 0

print(mom)