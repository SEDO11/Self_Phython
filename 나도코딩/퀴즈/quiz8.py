# 부동산 프로그램 작성

# 출력 예제
# 총 3대의 매물이 있다
# 강남 아파드 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

class House:
    # 매물 초기화
    # 매개변수 : 강남, 아파트, 매매, 10억, 2010년
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    
    # 매물 정보 표시
    def show_details(self):
        print("위치: {} / 타입: {} / 계약: {} / 가격: {} / 설립연도: {}".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))

k = House("강남", "아파트", "매매", "10억", "2010년")
m = House("마포", "오피스텔", "전세", "5억", "2007년")
s = House("송파", "빌라", "월세", "500/50", "2000년")

real_estate = []
real_estate.append(k)
real_estate.append(m)
real_estate.append(s)

print("총 {}대의 매물이 있습니다.".format(len(real_estate)))
for e in real_estate:
    e.show_details()
    