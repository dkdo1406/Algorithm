import sys
import bisect
input = lambda : sys.stdin.readline()

N, K, M = list(map(int, input().split()))
arr = []
L_set = set()
for _ in range(N):
    L = int(input())
    if L <= K or L == 2 * K:
        continue
    if L < 2 * K:
        arr.append(L - K)
        L_set.add(L - K)
    else:
        arr.append(L - 2 * K)
        L_set.add(L - 2 * K)

if not arr or sum(arr) < M:
    print(-1)
elif len(L_set) == 1 and sum(arr) >= M:
    print(arr[0])
else:
    n = len(arr)
    arr.sort()
    l = 1
    r = arr[-1]
    while l < r:
        c = (l + r) // 2
        cnt = 0
        i = 1
        while arr[-1] >= c * i:
            index = bisect.bisect_left(arr, c * i)
            cnt += (n - index)
            i += 1

        if cnt >= M:
            l = c + 1
        else:
            r = c

    print(l-1)