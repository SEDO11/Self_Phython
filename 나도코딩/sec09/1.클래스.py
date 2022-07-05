# # 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
# name = "마린" # 이름
# hp = 40 # 체력
# damage = 5 # 공격력

# print("{} 유닛이 생성되었습니다.".format(name))
# print("{} 체력, {} 공격력\n".format(hp, damage))

# # 탱크: 공격 유닛, 탱크, 포를 쏠 수 있다, 일반모드 / 시즈모드
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("{} 체력, {} 공격력\n".format(tank_hp, tank_damage))

# def attack(name, location, damage):
#     print("{} : {} 방향으로 적군을 공격합니다. [공격력 {}]".format(name, location, damage))
    
# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage) 

from tkinter import W


class Unit:
    def __init__(self, name, hp, damage): # 파이썬의 생성자
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {}, 공격력 {}".format(self.hp, self.damage))

# 마린, 탱크
# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# 레이스 : 클로킹
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름: {}, 공격력 : {} ".format(wraith1.name, wraith1.damage))

# 마컨 : 상대방 유닛을 내 것으로 만듬
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True # 외부에서 clocking(변수)를 추가로 할당하여 사용가능

if wraith2.clocking == True:
    print("{} 는 현재 클로킹 상태입니다.".format(wraith2.name))