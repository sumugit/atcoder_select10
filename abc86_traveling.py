import sys

N = int(input())

t = [0]
xy = []
for i in range(N):
    _t, _x, _y = map(int, input().split())
    t.append(_t)
    xy.append([_x, _y])

now = [0, 0]

for i in range(N):
    leng = abs(xy[i][0] - now[0]) + abs(xy[i][1] - now[1])
    if t[i+1] - t[i] >= leng:
        if leng % 2 == 1 and (t[i+1] - t[i]) % 2 == 1:
            now = xy[i]
        elif leng % 2 == 0 and (t[i+1] - t[i]) % 2 == 0:
            now = xy[i]
        else:
            print('No')
            exit()
    else:
        print('No')
        exit()

print('Yes')
