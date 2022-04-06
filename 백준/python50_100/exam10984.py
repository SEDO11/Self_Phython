#학점 계산

run = int(input())
for i in range(run):
    ct = 0
    gt = 0
    run2 = int(input())
    for j in range(run2):
        c, g = map(float, input().split())
        ct += int(c)
        gt += c * g
    gpa = gt / ct
    print("{} {:.1f}".format(ct, gpa))