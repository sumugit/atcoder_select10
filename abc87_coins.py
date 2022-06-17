a = int(input()) # 500
b = int(input()) # 100
c = int(input()) # 50
x = int(input())

cnt = 0
for i in range(a + 1):
    sum_a = 500 * i
    if sum_a > x:
        continue
    for j in range(b + 1):
        sum_b = sum_a + 100 * j
        if sum_b > x:
            break
        for k in range(c + 1):
            sum_c = sum_b + 50 * k
            if sum_c == x:
                cnt += 1

print(cnt)

# 10で割った余りで考える方法もある