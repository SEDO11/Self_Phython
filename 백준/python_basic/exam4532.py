#좀비의 뇌 먹방

run = int(input())

for i in range(run):
    list_bz = list(map(int, input().split()))
    brain = list_bz[0]
    zombie = list_bz[1]
    
    if brain >= zombie:
        print("MMM BRAINS")
    else :
        print("NO BRAINS")