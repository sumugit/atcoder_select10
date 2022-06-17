N = int(input())
a = list(map(int, input().split()))

sum_alice = 0
sum_bob = 0

"""
while len(a) != 0:
    num = max(a)
    sum_alice += num
    a.remove(num)
    if len(a) == 0:
        break
    num = max(a)
    sum_bob += num
    a.remove(num)

print(sum_alice - sum_bob)
"""

# sort 使う方が賢明
a.sort(reverse=True)
for i in range(len(a)):
    if i%2 == 0:
        sum_alice += a[i]
    else:
        sum_bob += a[i]

print(sum_alice - sum_bob)