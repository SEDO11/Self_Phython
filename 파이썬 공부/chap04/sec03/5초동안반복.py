import time

number = 0

target_tick = time.time() + 5 # 현재 시간에 5를 더해서 5초가 됨
while time.time() < target_tick:
    number += 1
    
print("5초 동안 {}번 반복했습니다.".format(number))