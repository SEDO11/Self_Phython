chicken = 10
waitng = 1

class SoldOutError(Exception):
    pass

while(True):
    try:
        print('[남은 치킨 : {}]'.format(chicken))
        order = int(input('치킨 몇 마리 주문하시겠습니까?'))
        if order > chicken: # 남은 치킨보다 주문량이 많을 때
            print('재료가 부족합니다.')
        elif order <= 0:
            raise ValueError
        else:
            print('[대기번호 {}] {} 마리 주문이 완료되었습니다.'.format(waitng, order))
            waitng += 1
            chicken -= order
            
        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print('잘못된 값을 입력하였습니다.')
    except SoldOutError:
        print('재고가 소진되어 더 이상 판매 할 수 없습니다.')
        break
    