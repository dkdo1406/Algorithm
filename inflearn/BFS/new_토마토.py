from collections import deque
C, R = list(map(int, input().split()))
graph = []
for r in range(R):
    graph.append(list(map(int, input().split())))

dr = [0,0,1,-1]
dc = [1,-1,0,0]
q = deque()
blank_count = 0
tomato = []
for r in range(R):
    for c in range(C):
        if graph[r][c] == 1:
            q.append((r,c))
        if graph[r][c] == -1:
            blank_count += 1
        if graph[r][c] == 0:
            tomato.append((r, c))

def BFS(q):
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c
            if nr < 0 or nr >= R or nc < 0 or nc >= C or graph[nr][nc] != 0:
                continue
            graph[nr][nc] = graph[r][c] + 1
            q.append((nr, nc))

answer = 1
if len(q) + blank_count == C * R:
    print(0)
else:
    for r,c in tomato:
        cnt = 0
        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c
            if nr < 0 or nr >= R or nc < 0 or nc >= C or graph[nr][nc] == -1:
                continue
            cnt += 1
        if cnt == 0:
            answer = 0
            break
    if answer != 0:
        BFS(q)
        for r in range(R):
            for c in range(C):
                if graph[r][c] == 0:
                    answer = 0
                elif graph[r][c] != 0 and answer != 0:
                    answer = max(answer, graph[r][c])
    print(answer-1)
