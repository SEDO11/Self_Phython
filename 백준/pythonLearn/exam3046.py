# 최솟값(r1)과 평균값(s)으로 최댓값(R2)구하기

rs = input().split() #공백으로 r1과 s 값자르기

r1 = int(rs[0])
s = int(rs[1])

r2 = (2 * s) - r1
print(r2)