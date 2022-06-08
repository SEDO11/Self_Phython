#Error Detection
import sys
t = int(sys.stdin.readline())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().strip().split())
    a = str(bin(a)).count('1') % 2
    if a == b:
        print('Valid')
    else:
        print('Corrupt')