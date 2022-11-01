#상하좌우

n = int(input())
min_x = 1
min_y = 1
max_x = n
max_y = n
l = list(map(str, input().split()))
x, y = 1, 1
for i in l:
    if i == 'R':
        x += 1
        if not min_x <= x <= max_x:
            x -= 1
    elif i == 'U':
        y -= 1
        if not min_y <= y <= max_y:
            y += 1
    elif i == 'D':
        y += 1
        if not min_y <= y <= max_y:
            y -= 1
    elif i == 'L':
        x -= 1
        if not min_x <= x <= max_x:
            x += 1
print(y, x)