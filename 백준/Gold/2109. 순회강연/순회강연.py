import heapq
n = int(input())
arr = []
for _ in range(n):
    p, d = list(map(int, input().split()))
    arr.append((p, d))
arr.sort(key=lambda x: x[1])
ans = 0
h = []
for p, d in arr:
    if not h or len(h) < d:
        heapq.heappush(h, (p, d))
    else:
        pay, day = heapq.heappop(h)
        if pay < p:
            heapq.heappush(h, (p, d))
        else:
            heapq.heappush(h, (pay, day))

for p, d in h:
    ans += p

print(ans)