import heapq
from collections import deque
N, M, X = list(map(int, input().split()))
INF = 10 ** 10
graph = [[INF for _ in range(N+1)] for _ in range(N+1)]
roads = []
for i in range(N+1):
    roads.append([])
    graph[i][i] = 0

for _ in range(M):
    s, e, t = list(map(int, input().split()))
    roads[s].append([e, t])

h = []
for e, t in roads[X]:
    heapq.heappush(h, (t, e))

visit = set()
while h:
    t, e = heapq.heappop(h)
    if graph[X][e] > t:
        graph[X][e] = t
        for end, time in roads[e]:
            if graph[X][end] > time + t:
                heapq.heappush(h, (time + t, end))
for i in range(1, N+1):
    if i == X:
        continue
    for end, time in roads[i]:
        heapq.heappush(h, (time, end))
    while h:
        t, e = heapq.heappop(h)
        if graph[i][e] > t:
            graph[i][e] = t
            if e != X:
                for end, time in roads[e]:
                    if graph[i][end] > time + t:
                        heapq.heappush(h, (time + t, end))

ans = 0
for i in range(1, N+1):
    if i == X:
        continue
    ans = max(ans, graph[i][X] + graph[X][i])
print(ans)
