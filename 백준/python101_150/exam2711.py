#오타맨 고창영

run = int(input())
for _ in range(run):
    a, b = input().split()
    b = b[:int(a)-1] + b[int(a):]
    print(b)