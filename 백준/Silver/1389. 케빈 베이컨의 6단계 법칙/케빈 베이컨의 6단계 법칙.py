N, M = list(map(int, input().split()))
graph = [[N+1 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    s, e = list(map(int, input().split()))
    graph[s-1][e-1] = 1
    graph[e-1][s-1] = 1

for i in range(N):
    for j in range(N):
        for k in range(N):
            if j == k:
                continue
            if graph[j][k] > graph[j][i] + graph[i][k]:
                graph[j][k] = graph[j][i] + graph[i][k]
ans = [0, N*N]
for i in range(N):
    res = sum(graph[i])
    if ans[1] > res:
        ans = [i+1, res]

print(ans[0])
