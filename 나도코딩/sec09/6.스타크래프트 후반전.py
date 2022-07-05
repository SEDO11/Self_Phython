# 스타크래프트
# 자식 클래스에서 부모클래스의 생성자 호출
# 파이썬의 self는 자바에서 this이다.

from random import *

# 부모 클래스
# 유닛 생성
class Unit:
    def __init__(self, name, hp, speed): # 파이썬의 생성자
        self.name = name
        self.hp = hp
        self.speed = speed
        print("유닛 생성 : {} , 체력 : {}".format(self.name, self.hp))
        
    def move(self, location): # FlyableAttackUint 클래스의 move 메서드가 이 메서드를 오버라이딩 한다
        print("{} : {} 방향으로 이동합니다. [속도 {}]".format(self.name, location, self.speed))
        
    def damaged(self, damage): # 메서드
        print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {} 입니다.".format(self.name, self.hp if self.hp >= 0 else 0))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))

# 부모 클래스
# 공중 유닛 이동 속도
class Flyable:
    def __init__(self,flying_speed): # 생성자
        self.flying_speed = flying_speed
    
    def fly(self, name, location): # 메서드
        print("{} : {} 방향으로 날아갑니다. [속도 : {}]".format(name, location, self.flying_speed))

# 자식 클래스
# 공격 유닛
class AttackUnit(Unit): # AttackUnit은 Unit을 상속 받는다
    def __init__(self, name, hp, damage, speed): # 파이썬의 생성자
        Unit.__init__(self, name, hp, speed) # 부모 클래스의 필드 상속
        self.damage = damage
    
    def attack(self, location): # 메서드
        print("{} : {} 방향으로 적군을 공격 [공격력: {}]".format(self.name, location, self.damage))
        

#자식클래스, 다중 상속 클래스
#공중 공격 유닛
class FlyableAttackUint(AttackUnit, Flyable): # 다중 상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0) # 지상 speed 0
        Flyable.__init__(self, flying_speed)
        
    def move(self, location): # 메서드 오버라이딩
        self.fly(self.name, location)

# 마린 클래스
class Marine(AttackUnit):
    def __init__(self): # 생성자 
        super().__init__("마린", 40, 5, 1)
    
    #스팀팩, 공격속도, 공격력 증가, 체력 10 감소
    def steampack(self): # 메서드
        if self.hp > 10:
            self.hp -= 10
            print("{} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# 탱크 클래스
class Tank(AttackUnit):
    seize_developed = False # 시즈모드 개발 여부
    def __init__(self): # 생성자 
        super().__init__("탱크", 150, 35, 1)
        self.seize_mode = False # 시즈모드 여부
        
    #시즈모드, 이동x, 공격력 증가
    def set_seize_mode(self): # 메서드
        # 시즈모드가 개발되지 않았을 때
        if self.seize_developed == False:
            return
        # 시즈모드가 아닐 때 -> 시즈모드
        if self.seize_mode == False:
            print("{} : 시즈 모드로 전환합니다.".format(self.name))
            self.damage *= 2 
            self.seize_mode = True
        # 시즈모드가 일 때 -> 시즈모드 해제
        else:
            print("{} : 일반 모드로 전환합니다.".format(self.name))
            self.damage /= 2 
            self.seize_mode = False
            
#레이스
class Wraith(FlyableAttackUint):
    clocking_developed = False
    def __init__(self):
        super().__init__("레이스", 80, 20, 5)
        self.clocked = False
        
     #클로킹모드, 눈에 안뜸
    def set_clocking_mode(self): # 메서드
        # 클로킹모드가 개발되지 않았을 때
        if self.clocking_developed == False:
            return
        # 클로킹모드가 아닐 때 -> 클로킹모드
        if self.clocked == False:
            print("{} : 클로킹 모드로 전환합니다.".format(self.name))
            self.clocked = True
        # 클로킹모드가 일 때 -> 클로킹모드 해제
        else:
            print("{} : 일반 모드로 전환합니다.".format(self.name))
            self.clocked = False
            
    def damaged(self, damage): # 메서드
        if self.clocked == False:
            print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
            self.hp -= damage
            print("{} : 현재 체력은 {} 입니다.".format(self.name, self.hp if self.hp >= 0 else 0))
            if self.hp <= 0:
                print("{} : 파괴되었습니다.".format(self.name))
        else:
            print("{} 는 클로킹 모드라 공격을 받지 않습니다. ".format(self.name))

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")
    
def game_over():
    print("Player : GG")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")

# 실제 게임 진행
game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()
            
t1 = Tank()
t2 = Tank()

w1 = Wraith()

#유닛 일괄 관리
attack_unit = []
attack_unit.append(m1)
attack_unit.append(m2)
attack_unit.append(m3)
attack_unit.append(t1)
attack_unit.append(t2)
attack_unit.append(w1)

# 전군 이동
for units in attack_unit:
    units.move("1시")
    
# 탱크 시즈모드, 레이스 클로킹 개발
Tank.seize_developed = True
Wraith.clocking_developed = True

# 공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
for units in attack_unit:
    # if units.name == "마린":
    #     units.steampack()
    # elif units.name == "탱크" and Tank.seize_developed == True:
    #     units.set_seize_mode()
    # elif units.name == "레이스" and Wraith.clocking_developed == True:
    #     units.set_clocking_mode()
    if isinstance(units, Marine): # 해당 인스턴스가 Marine 인 경우
        units.steampack()
    elif isinstance(units, Tank): # 해당 인스턴스가 Tank 인 경우
        units.set_seize_mode()
    elif isinstance(units, Wraith): # 해당 인스턴스가 Wraith 인 경우
        units.set_clocking_mode()
        
# 공격
for units in attack_unit:
    units.attack("5시")

w1.set_clocking_mode() # 클로킹 모드 해제

# 전군 피해
for units in attack_unit:
    units.damaged(randint(5, 21)) # 공격은 랜덤으로 받음(5~20)