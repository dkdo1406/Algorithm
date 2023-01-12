from collections import deque
n, m = list(map(int, input().split()))
graph = [list(map(int, input())) for _ in range(n)]

dr = [1,-1,0,0]
dc = [0,0,-1,1]

def BFS():
    q = deque()
    q.append([0,0])
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c
            if nr < 0 or nr >= n or nc < 0 or nc >= m or graph[nr][nc] != 1:
                continue
            graph[nr][nc] += graph[r][c]
            q.append([nr, nc])
BFS()
print(graph[n-1][m-1])