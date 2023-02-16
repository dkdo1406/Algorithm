from collections import deque
M, N = list(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(N)]

dr = [0,0,1,-1]
dc = [1,-1,0,0]

def bfs():
    q = deque()
    for i in tomato:
        q.append(i)
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= M or graph[nr][nc] == -1 or graph[nr][nc] == 1:
                continue
            if graph[nr][nc] == 0 or graph[nr][nc] > graph[r][c] + 1:
                graph[nr][nc] = graph[r][c] + 1
                q.append((nr, nc))
tomato = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            tomato.append((i, j))
if tomato:
    bfs()

def check():
    ans = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                return -1
            ans = max(ans, graph[i][j])
    return ans - 1
print(check())