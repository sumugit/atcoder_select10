import sys

N, Y = map(int, input().split())


for x in range(N+1):
    moy = 10000 * x
    if moy > Y:
        break
    elif moy + 5000 * (N - x) < Y:
        continue
    for y in range(N - x + 1):
        moy = 10000 * x + 5000 * y + 1000 * (N - x - y)
        if moy == Y:
            print(f'{x} {y} {N - x - y}')
            sys.exit(0)

print('-1 -1 -1')