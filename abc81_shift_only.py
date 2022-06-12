n = int(input())
a = list(map(int, input().split()))

flag = False
num = 0
while True:
    if not flag:
        for i in range(len(a)):
            if a[i] % 2 == 1:
                print(0)
                exit()
            else:
                a[i] /= 2
        flag = True
    else:
        for i in range(len(a)):
            if a[i] % 2 == 1:
                print(num)
                exit()
            else:
                a[i] /= 2
    num += 1