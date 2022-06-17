N, a, b = map(int, input().split())

ans = 0

for n in range(1, N+1):
    s = str(n)
    sum_digits = sum(list(map(int, s)))
    if a <= sum_digits <= b:
        ans += n

print(ans)