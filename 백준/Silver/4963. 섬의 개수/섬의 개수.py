from collections import deque
while True:
    w, h = list(map(int, input().split()))
    if w ==0 and h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]

    dr = [1,-1,0,0,1,1,-1,-1]
    dc = [0,0,-1,1,1,-1,1,-1]
    answer = 0
    def BFS(r,c):
        q = deque()
        q.append([r,c])
        graph[r][c] = 0
        while q:
            r, c = q.popleft()
            for i in range(8):
                nr = dr[i] + r
                nc = dc[i] + c
                if nr < 0 or nr >= h or nc < 0 or nc >= w or graph[nr][nc] == 0:
                    continue
                graph[nr][nc] = 0
                q.append([nr, nc])
    for r in range(h):
        for c in range(w):
            if graph[r][c] == 1:
                BFS(r,c)
                answer += 1
    print(answer)
