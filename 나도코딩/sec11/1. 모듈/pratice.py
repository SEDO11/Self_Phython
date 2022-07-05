import theater_module as tm

tm.price(5) # 5명이서 영화를 보러 갔을 때
tm.price_morning(10) # 10명이서 조조 영화를 보러갔을 때
tm.price_soldier(2) # 군인 2명이서 영화를 보러갔을 때

from theater_module import * # 모듈내의 모든 함수 사용

price(5)
price_morning(10)
price_soldier(2)

from theater_module import price_soldier as price # price_soldier함스를 price로 이용
price(5)