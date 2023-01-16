from collections import deque
n, m = list(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(n)]

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def BFS(r,c):
    q = deque()
    q.append([r,c])
    graph[r][c] = 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c
            if nr < 0:
                nr = n-1
            if nc < 0:
                nc = m-1
            if nr == n:
                nr = 0
            if nc == m:
                nc = 0
            if graph[nr][nc] == 1:
                continue
            graph[nr][nc] = 1
            q.append([nr, nc])
answer = 0
for r in range(n):
    for c in range(m):
        if graph[r][c] == 0:
            BFS(r,c)
            answer += 1

print(answer)