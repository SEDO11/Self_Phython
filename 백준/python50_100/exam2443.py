#별찍기 6

star = int(input())
for i in range(star-1, 0, -1):
    print(" "*(star-i)+"*"*(2*i-1))