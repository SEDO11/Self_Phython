# 상속, 다중상속
# 파이썬의 self는 자바에서 this이다.

# 부모 클래스
# 유닛 생성
class Unit:
    def __init__(self, name, hp): # 파이썬의 생성자
        self.name = name
        self.hp = hp
        print("유닛 생성 : {} , 체력 : {}\n".format(self.name, self.hp))

# 부모 클래스
# 공중 유닛 이동 속도
class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{} : {} 방향으로 날아갑니다. [속도 : {}]".format(name, location, self.flying_speed))

# 자식 클래스
# 공격 유닛
class AttackUnit(Unit): # AttackUnit은 Unit을 상속 받는다
    def __init__(self, name, hp, damage): # 파이썬의 생성자
        Unit.__init__(self, name, hp) # 부모 클래스의 필드 상속
        self.damage = damage
    
    def attack(self, location): # 메서드
        print("{} : {} 방향으로 적군을 공격 [공격력: {}]\n".format(self.name, location, self.damage))
        
    def damaged(self, damage): # 메서드
        print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {} 입니다.\n".format(self.name, self.hp if self.hp >= 0 else 0))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.\n".format(self.name))

#자식클래스, 다중 상속 클래스
#공중 공격 유닛
class FlyableAttackUint(AttackUnit, Flyable): # 다중 상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

# #메딕
# medic = Unit("메딕1", 60)

# #파이어뱃
# firebat = AttackUnit("파이어뱃1", 50, 16)
# firebat.attack("1시")
# while firebat.hp > 0:
#     firebat.damaged(25)
    
# 레이스
wraith1 = FlyableAttackUint("레이스1", 80, 20, 30)
wraith1.fly(wraith1.name, "10시")
while wraith1.hp >= 0:
    wraith1.damaged(25)