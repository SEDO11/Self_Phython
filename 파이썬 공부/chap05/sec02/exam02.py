# 100명이 하나 이상의 테이블에 나눠서 앉음
# 한 명이 한 테이블에 앉을 수는 없음
# 최소 두 명 이상
# 22222 / 2233 / 334 / 55/ 64/ 82 / 10

mini = 2 # 앉힐 수 있는 최소 사람 수
maxi = 10 # 앉힐 수 있는 최대 사람 수
alli = 100 # 전체 사람의 수
count = 0 # 출력

def cal(remain, used): # 남은 사람 수, 앉힐 수 있는 최소 사람 수
    global count
    # 종료 조건
    if remain < 0: # 남은 사람 수가 0보다 작을 때
        # 제대로된 경우x
        return 0
    if remain == 0: # 남은 사람 수가 0
        count += 1
        # 제대로된 경우o
        return 1
    #재귀처리
    for i in range(used, maxi+1):
        cal(remain - i, i)
    return 
    #메모화 처리
    
    #종료
    
cal(alli, mini)
print(count)