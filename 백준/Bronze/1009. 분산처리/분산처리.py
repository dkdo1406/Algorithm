n = int(input())
for _ in range(n):
    a, b = list(map(int, input().split()))
    if a % 10 == 0:
        print(10)
    elif b % 4 == 0:
        print(a ** 4 % 10)
    else:
        print((a ** (b % 4)) % 10)