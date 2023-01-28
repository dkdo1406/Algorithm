from collections import deque
n = int(input())
graph = [list(map(int, list(input()))) for _ in range(n)]

dr = [0,0,1,-1]
dc = [1,-1,0,0]

def bfs(r, c):
    q = deque()
    q.append([r, c])
    graph[r][c] = 0
    count = 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c

            if nr < 0 or nr >= n or nc < 0 or nc >= n or graph[nr][nc] == 0:
                continue
            q.append([nr, nc])
            graph[nr][nc] = 0
            count += 1
    return count
cnt = 0
answer = []
for r in range(n):
    for c in range(n):
        if graph[r][c] == 1:
            cnt += 1
            answer.append(bfs(r, c))
answer.sort()
print(cnt)
for i in answer:
    print(i)