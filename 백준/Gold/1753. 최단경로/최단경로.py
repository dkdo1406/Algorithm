import sys
input = lambda : sys.stdin.readline()
import heapq

V, E = list(map(int, input().split()))
graph = [[] for _ in range(V)]

INF = int(1e9)
ans = [INF for _ in range(V)]
start = int(input()) - 1

for _ in range(E):
    u, v, w = list(map(int, input().split()))
    graph[u-1].append([v-1, w])

ans[start] = 0

q = []
heapq.heappush(q, (0, start))
while q:
    dist, now = heapq.heappop(q)
    if ans[now] < dist:
        continue
    for i, j in graph[now]:
        cost = dist + j
        if cost < ans[i]:
            ans[i] = cost
            heapq.heappush(q, (cost, i))

for i in ans:
    if i == INF:
        print("INF")
    else:
        print(i)


