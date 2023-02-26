from collections import deque
N, M = list(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(N)]

ans = 0
dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]

def bfs(R, C):
    global ans
    q = deque()
    q.append((R, C, 0))
    visit = set()
    visit.add((R, C))
    while q:
        r, c, L = q.popleft()
        if graph[r][c] == 1:
            ans = max(ans, L)
            return
        for i in range(8):
            nr = dr[i] + r
            nc = dc[i] + c
            if nr < 0 or nr >= N or nc < 0 or nc >= M or (nr, nc) in visit:
                continue
            q.append((nr, nc, L + 1))
            visit.add((nr, nc))
for r in range(N):
    for c in range(M):
        bfs(r, c)
print(ans)