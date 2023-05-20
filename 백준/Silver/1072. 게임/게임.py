import math
X, Y = list(map(int, input().split()))
if X == 0:
    print(1)
else:
    Z = math.floor(Y * 100 / X)
    ans = 0
    INF = 10 ** 15
    l = 0
    r = INF
    while l < r:
        c = (l + r) // 2
        if Z == math.floor((Y + c) * 100 / (X + c)):
            l = c + 1
        else:
            r = c
            ans = r
    if ans == 0:
        print(-1)
    else:
        print(ans)