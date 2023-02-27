R, C, T = list(map(int, input().split()))

graph = [list(map(int, input().split())) for _ in range(R)]


def spread(r, c):
    global graph
    dust = graph[r][c] // 5
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    cnt = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= R or nc < 0 or nc >= C or graph[nr][nc] == -1:
            continue
        spread_graph[nr][nc] += dust
        cnt += 1
    graph[r][c] -= dust * cnt

def filtter(r):
    global graph
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]
    i = 0
    nr = r + dr[i]
    nc = 0 + dc[i]
    wind = 0
    dust = graph[nr][nc] # 이동할 값
    graph[nr][nc] = wind # 이전 값
    wind = dust

    while i < 4:
        nr += dr[i]
        nc += dc[i]
        if nr == -1:
            nr = 0
            i += 1
            nr += dr[i]
            nc += dc[i]
        elif nr == R:
            nr -= 1
            i += 1
            nr += dr[i]
            nc += dc[i]
        elif nc == -1:
            nc = 0
            i += 1
            nr += dr[i]
            nc += dc[i]
        elif nc == C:
            nc -= 1
            i += 1
            nr += dr[i]
            nc += dc[i]
        if i == 3:
            if graph[nr][nc] == -1:
                break
        dust = graph[nr][nc] # 이동할 값
        graph[nr][nc] = wind # 이전 값
        wind = dust
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    i = 0
    nr = r + dr[i] + 1
    nc = 0 + dc[i]
    wind = 0
    dust = graph[nr][nc]  # 이동할 값
    graph[nr][nc] = wind  # 이전 값
    wind = dust
    while i < 4:
        nr += dr[i]
        nc += dc[i]
        if nr == -1:
            nr = 0
            i += 1
            nr += dr[i]
            nc += dc[i]
        elif nr == R:
            nr -= 1
            i += 1
            nr += dr[i]
            nc += dc[i]
        elif nc == -1:
            nc = 0
            i += 1
            nr += dr[i]
            nc += dc[i]
        elif nc == C:
            nc -= 1
            i += 1
            nr += dr[i]
            nc += dc[i]
        if i == 3:
            if graph[nr][nc] == -1:
                break
        dust = graph[nr][nc]  # 이동할 값
        graph[nr][nc] = wind  # 이전 값
        wind = dust

for _ in range(T):
    spread_graph = [[0 for _ in range(C)]for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if graph[r][c] > 4:
                spread(r, c)

    for r in range(R):
        for c in range(C):
            graph[r][c] += spread_graph[r][c]


    for r in range(R):
        if graph[r][0] == -1:
            filtter(r)
            break
ans = 2
for i in graph:
    ans += sum(i)
print(ans)
