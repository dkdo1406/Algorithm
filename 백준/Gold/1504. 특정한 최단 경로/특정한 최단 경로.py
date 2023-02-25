import sys
import heapq
input = lambda : sys.stdin.readline()
N, E = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(E):
    s, e, d = list(map(int, input().split()))
    graph[s-1].append([e-1, d])
    graph[e - 1].append([s - 1, d])

a, b = list(map(int, input().split()))
visit = [a-1, b-1]

INF = int(10e10)
hq = []
ans_1 = [INF] * N
ans_1[visit[0]] = 0
heapq.heappush(hq, (0, visit[0]))
while hq:
    dist, now = heapq.heappop(hq)
    if ans_1[now] < dist:
        continue
    for i, j in graph[now]:
        cost = dist + j
        if cost < ans_1[i]:
            ans_1[i] = cost
            heapq.heappush(hq, (cost, i))

hq = []
ans_2 = [INF] * N
ans_2[visit[1]] = 0
heapq.heappush(hq, (0, visit[1]))
while hq:
    dist, now = heapq.heappop(hq)
    if ans_2[now] < dist:
        continue
    for i, j in graph[now]:
        cost = dist + j
        if cost < ans_2[i]:
            ans_2[i] = cost
            heapq.heappush(hq, (cost, i))
ans = 0
if (ans_1[0] == INF and ans_2[0] == INF) or (ans_1[N-1] == INF and ans_2[N-1] == INF) or ans_1[visit[1]] == INF:
    ans = -1
else:
    if ans_1[0] == INF or ans_2[N-1] == INF:
        ans = ans_1[N-1] + ans_2[0]
    elif ans_1[N-1] == INF or ans_2[0] == INF:
        ans = ans_1[0] + ans_2[N-1]
    else:
        ans = min(ans_1[0] + ans_2[N-1], ans_1[N-1] + ans_2[0])
    ans += ans_1[visit[1]]
print(ans)