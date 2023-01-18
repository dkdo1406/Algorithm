from collections import deque
T = int(input())

def BFS(i, j):
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    q = deque()
    q.append([i, j])
    graph[i][j] = 0
    while q:
        rr, cc = q.popleft()
        for i in range(4):
            nr = dr[i] + rr
            nc = dc[i] + cc
            if nr < 0 or nr >= r or nc < 0 or nc >= c or graph[nr][nc] == 0:
                continue
            q.append([nr, nc])
            graph[nr][nc] = 0
for _ in range(T):
    c, r, k = list(map(int, input().split()))
    graph = [[0 for _ in range(c)] for _ in range(r)]
    for _ in range(k):
        i, j = list(map(int, input().split()))
        graph[j][i] = 1

    answer = 0
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 1:
                BFS(i, j)
                answer += 1
    print(answer)