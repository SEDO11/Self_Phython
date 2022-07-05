# 오버라이딩
# 파이썬의 self는 자바에서 this이다.

# 부모 클래스
# 유닛 생성
class Unit:
    def __init__(self, name, hp, speed): # 파이썬의 생성자
        self.name = name
        self.hp = hp
        self.speed = speed
        print("유닛 생성 : {} , 체력 : {}\n".format(self.name, self.hp))
        
    def move(self, location): # FlyableAttackUint 클래스의 move 메서드가 이 메서드를 오버라이딩 한다
        print("[지상 유닛 이동]")
        print("{} : {} 방향으로 이동합니다. [속도 {}]".format(self.name, location, self.speed))

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
    def __init__(self, name, hp, damage, speed): # 파이썬의 생성자
        Unit.__init__(self, name, hp, speed) # 부모 클래스의 필드 상속
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
        AttackUnit.__init__(self, name, hp, damage, 0) # 지상 speed 0
        Flyable.__init__(self, flying_speed)
        
    def move(self, location): # 메서드 오버라이딩
        print("[공중 유닛 이동]")
        self.fly(self.name, location)
        
# 벌처
vulture = AttackUnit("벌쳐", 80, 10, 20)

#배틀크루져
battlecruiser = FlyableAttackUint("배틀크루져", 500, 25, 3)
battleship = FlyableAttackUint("배틀쉽", 200, 0, 10)

vulture.move("11시")
battlecruiser.move("9시")
battleship.move("3시")