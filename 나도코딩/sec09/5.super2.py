# super 유의사항
# 다중 상속일 때에는 super를 사용하면 논리 오류가 생김

class Unit:
    def __init__(self):
        print("Unit 생성자")
    
class Flyable:
    def __init__(self):
        print("Flyable 생성자")
        
class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__()
        Flyable.__init__(self)

# 드랍쉽
dropship = FlyableUnit()
        