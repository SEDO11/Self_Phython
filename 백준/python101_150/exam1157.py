#단어 공부
s = input()
l = []
for i in range(65, 91):
    l.append([s.count(chr(i)) + s.count(chr(i+32)), chr(i)])
l.sort(reverse=True)
if l[0][0] == l[1][0]:
  r = "?"
else:
  r = l[0][1]
print(r)