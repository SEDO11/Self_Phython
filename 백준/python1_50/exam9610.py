# 사분면

run = int(input())
q1 = 0
q2 = 0
q3 = 0
q4 = 0
axis = 0 
for i in range(run):
    list_xy = input().split()
    
    x = int(list_xy[0])
    y = int(list_xy[1])
    
    if x > 0 and y > 0: #1 사분면
        q1 += 1
    elif x < 0 and y > 0: #2 사분면
        q2 += 1
    elif x < 0 and y < 0: #3 사분면
        q3 += 1
    elif x > 0 and y < 0: #4 사분면
        q4 += 1
    else : # 0이 들어가있는 경우
        axis += 1 
        
print("Q1:",q1)
print("Q2:",q2)
print("Q3:",q3)
print("Q4:",q4)
print("AXIS:",axis)