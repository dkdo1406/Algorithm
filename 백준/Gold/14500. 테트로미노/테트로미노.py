import copy

N, M = list(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(N)]

answer = 0
dr = [0,0,1,-1]
dc = [1,-1,0,0]
visited = [([0] * M) for _ in range(N)]
def DFS(L, r, c, result):
    global answer
    if L == 3:
        answer = max(answer, result)
        return
    for i in range(4):
        nr = dr[i] + r
        nc = dc[i] + c
        if nr < 0 or nr >= N or nc < 0 or nc >= M or visited[nr][nc] == 1:
            continue
        if L == 1:
            visited[nr][nc] = 1
            DFS(L + 1, r, c,  result + graph[nr][nc])
            visited[nr][nc] = 0
        visited[nr][nc] = 1
        DFS(L+1, nr, nc, result + graph[nr][nc])
        visited[nr][nc] = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        DFS(0, i, j, graph[i][j])
        visited[i][j] = 0
print(answer)
