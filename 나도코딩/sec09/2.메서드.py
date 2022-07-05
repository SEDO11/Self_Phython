# 메서드
# 파이썬의 self는 자바에서 this이다.

class Unit:
    def __init__(self, name, hp, damage): # 파이썬의 생성자
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {}, 공격력 {}".format(self.hp, self.damage))
        
class AttackUnit:
    def __init__(self, name, hp, damage): # 파이썬의 생성자
        self.name = name
        self.hp = hp
        self.damage = damage
    
    def attack(self, location): # 메서드
        print("{} : {} 방향으로 적군을 공격 [공격력: {}]\n".format(self.name, location, self.damage))
        
    def damaged(self, damage): # 메서드
        print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {} 입니다.\n".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.\n".format(self.name))

#파이어뱃
firebat = AttackUnit("파이어뱃1", 50, 16)
firebat.attack("1시")
while firebat.hp > 0:
    firebat.damaged(25)