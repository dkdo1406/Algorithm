import sys
input = lambda: sys.stdin.readline()
N, M = list(map(int, input().split()))

day = []

for _ in range(N):
    money = int(input())
    day.append(money)

l = 0
r = 1000000000
res = 0

def check(mid):
    start = mid
    cnt = 1
    for i in day:
        if start >= i:
            start -= i
        else:
            cnt += 1
            start = mid
            if start < i:
                return False
            start -= i

    return cnt <= M


while l <= r:
    c = (l + r) // 2
    if check(c):
        r = c - 1
        res = c
    else:
        l = c + 1

print(res)