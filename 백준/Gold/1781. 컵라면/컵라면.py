import sys
import heapq
input = lambda: sys.stdin.readline()
n = int(input())
arr = []
for _ in range(n):
    d, p = list(map(int, input().split()))
    arr.append((d, p))
arr.sort(key=lambda x: x[0])
ans = 0
h = []
for d, p in arr:
    if not h or len(h) < d:
        heapq.heappush(h, (p, d))
        ans += p
    else:
        pay, day = heapq.heappop(h)
        if pay < p:
            heapq.heappush(h, (p, d))
            ans -= pay
            ans += p
        else:
            heapq.heappush(h, (pay, day))

print(ans)