import sys
import heapq
input = lambda: sys.stdin.readline()
N, K = list(map(int, input().split()))

arr = []
for _ in range(N):
    M, V = list(map(int, input().split()))
    arr.append((M, V))
arr.sort()
bags = []
for i in range(K):
    bags.append(int(input()))
bags.sort()

ans = 0
gem = []

i = 0
for bag in bags:
    while i < N:
        m, v = arr[i]
        if m > bag:
            break
        heapq.heappush(gem, -v)
        i += 1
    if gem:
        ans -= heapq.heappop(gem)

print(ans)