from travel_temp import *

trip_to2 = thailand.ThailandPackage()
trip_to2.detail()

# 패키지, 모듈 위치 불러오기
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))
