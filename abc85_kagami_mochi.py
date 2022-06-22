N = int(input())
d = []
for n in range(N):
    d.append(int(input()))

d.sort()

ans = 0
for idx in range(len(d)):
    if idx == 0:
        ans += 1
    else:
        if d[idx] != d[idx-1]:
            ans += 1

print(ans)
