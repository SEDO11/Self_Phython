mini = 2
maxi = 10
alli = 100
memo = {}

def cal(remain, used):
    key = str([remain, used])
    
    # 종료 조건
    if key in memo:
        pass
    if remain < 0:
        return 0
    if remain == 0:
        return 1
    #재귀처리
    
    #메모화 처리
    
    #종료
    
print(cal(alli, mini))