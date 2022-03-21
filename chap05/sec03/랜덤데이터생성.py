#랜덤한 숫자를 만들기 위해 import
import random

#간단한 한글 리스트 만듬
hanguls = list("가나다라마바사아자차카타파하")

#파일을 쓰기 모드로 엽니다.
with open("chap05\\sec03\\random_user_create.txt", "w") as file:
    for i in range(1000):
        # 랜덤한 값으로 변수를 생성합니다.
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)
        
        file.write("{}, {}, {}\n".format(name, weight, height))
        
