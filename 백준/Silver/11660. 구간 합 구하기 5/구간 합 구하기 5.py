import sys
input = lambda: sys.stdin.readline()

N, M = list(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(N)]

for r in range(N - 2, -1, -1):
    graph[r][N - 1] += graph[r + 1][N - 1]
    graph[N - 1][r] += graph[N - 1][r + 1]
for r in range(N - 2, -1, -1):
    for c in range(N - 2, -1, -1):
        graph[r][c] += graph[r + 1][c] + graph[r][c + 1] - graph[r + 1][c + 1]

for _ in range(M):
    r1, c1, r2, c2 = list(map(int, input().split()))
    res = graph[r1-1][c1-1]
    if r2 != N and c2 != N:
        res += graph[r2][c2] - graph[r2][c1-1] - graph[r1-1][c2]
    elif r2 != N:
        res -= graph[r2][c1-1]
    elif c2 != N:
        res -= graph[r1-1][c2]
    print(res)