#FBI
import sys
r = ""
for i in range(1, 6):
    s = sys.stdin.readline().strip()
    if "FBI" in s:
        r += str(i) + " "
if len(r) == 0:
    print("HE GOT AWAY!")
else:
    print(r)