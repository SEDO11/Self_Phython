string = input().split(" ")
string.sort(reverse=True)
dice1 = int(string[0])
dice2 = int(string[1])
dice3 = int(string[2])
result = 0
money1 = 10000
money2 = 1000
money3 = 100

# 모두다 같은 경우
if dice1 == dice2 and dice2 == dice3:
    result = money1 + dice1 * money2
# 두 개만 같은 경우
elif dice1 == dice2 or dice1 == dice3:
    result = money2 + dice1 * money3
elif dice2 == dice3:
    result = money2 + dice2 * money3
# 같은 게 없는 경우
else:
    result = dice1 * money3
    
print(result)