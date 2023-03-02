from collections import deque
R, C, K = list(map(int, input().split()))

graph = [list(map(int, input().split())) for _ in range(R)]
tem_graph = [[0 for _ in range(C)] for _ in range(R)]
wall_cnt = int(input())
ans = 0
walls = [list(map(int, input().split())) for _ in range(wall_cnt)]
wall_0 = set()
wall_1 = set()
for r, c, i in walls:
    if i == 0:
        wall_0.add((r-1, c-1))
    elif i == 1:
        wall_1.add((r-1, c-1))
heats = []
tem = []
for r in range(R):
    for c in range(C):
        if graph[r][c] == 0:
            continue
        if graph[r][c] == 5:
            tem.append([r, c])
        else:
            heats.append([r, c, graph[r][c]])

def heater(r, c, d):
    global tem_graph
    copy_graph = [[0 for _ in range(C)] for _ in range(R)]
    dr = [0, 0, 0, -1, 1]
    dc = [0, 1, -1, 0, 0]

    if d < 3:
        ddr = [0, 1, -1]
        ddc = [0, 0, 0]
    else:
        ddr = [0, 0, 0]
        ddc = [0, 1, -1]

    nr = r + dr[d]
    nc = c + dc[d]
    copy_graph[nr][nc] += 5
    # 벽이 0 인 경우에 위, 아래에 영향 wall_0
    # 벽이 1 인 경우에 좌, 우에 영향 wall_1
    q = deque()
    q.append((nr, nc, copy_graph[nr][nc] - 1))
    # 대각선으로 이동할 때
    # 1) 옆으로 이동 시 벽에 부딪치지 않는가
    # 2) 원래 가는 방향으로 갈 때 부딪치지 않는가

    visit = set()
    while q:
        r, c, temperature, = q.popleft()
        if temperature == 0:
            continue
        for i in range(3):
            if i == 0:
                nr = r + dr[d]
                nc = c + dc[d]
                if nr < 0 or nr >= R or nc < 0 or nc >= C:
                    continue
                if d == 1 and (r, c) in wall_1:
                    continue
                elif d == 2 and (nr, nc) in wall_1:
                    continue
                elif d == 3 and (r, c) in wall_0:
                    continue
                elif d == 4 and (nr, nc) in wall_0:
                    continue
            else:
                next_r = r + ddr[i]
                next_c = c + ddc[i]
                if next_r < 0 or next_r >= R or next_c < 0 or next_c >= C or (next_r, next_c) in visit:
                    continue
                if d == 1 or d == 2:
                    if i == 1 and (next_r, next_c) in wall_0:
                        continue
                    elif i == 2 and (r, c) in wall_0:
                        continue
                else:
                    if i == 1 and (r, c) in wall_1:
                        continue
                    elif i == 2 and (next_r, next_c) in wall_1:
                        continue

                nr = next_r + dr[d]
                nc = next_c + dc[d]
                if nr < 0 or nr >= R or nc < 0 or nc >= C:
                    continue
                if d == 1 and (next_r, next_c) in wall_1:
                    continue
                elif d == 2 and (nr, nc) in wall_1:
                    continue
                elif d == 3 and (next_r, next_c) in wall_0:
                    continue
                elif d == 4 and (nr, nc) in wall_0:
                    continue
            if (nr, nc) in visit:
                continue
            copy_graph[nr][nc] += temperature
            visit.add((nr, nc))
            q.append((nr, nc, temperature - 1))

    for r in range(R):
        for c in range(C):
            tem_graph[r][c] += copy_graph[r][c]

def balance(r, c):
    global temp_graph
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    value = tem_graph[r][c]
    for i in range(4):
        nr = dr[i] + r
        nc = dc[i] + c
        if nr < 0 or nr >= R or nc < 0 or nc >= C or value - tem_graph[nr][nc] < 4:
            continue
        if i == 0 and (nr, nc) in wall_0:
            continue
        elif i == 1 and (r, c) in wall_0:
            continue
        elif i == 2 and (r, c) in wall_1:
            continue
        elif i == 3 and (nr, nc) in wall_1:
            continue
        val = (tem_graph[r][c] - tem_graph[nr][nc]) // 4
        temp_graph[nr][nc] += val
        temp_graph[r][c] -= val


def check():
    for r, c in tem:
        if tem_graph[r][c] < K:
            return False
    return True


while ans < 101:
    for r, c, d in heats:
        heater(r, c, d)

    temp_graph = [[0 for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if tem_graph[r][c] > 3:
                balance(r, c)
    for r in range(R):
        for c in range(C):
            tem_graph[r][c] += temp_graph[r][c]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    r, c, i = 0, 1, 0
    while r != -1:
        if tem_graph[r][c] > 0:
            tem_graph[r][c] -= 1
        r += dr[i]
        c += dc[i]
        if c == C:
            c -= 1
            i += 1
            r += dr[i]
            c += dc[i]
        if r == R:
            r -= 1
            i += 1
            r += dr[i]
            c += dc[i]
        if c == -1:
            c = 0
            i += 1
            r += dr[i]
            c += dc[i]
    ans += 1

    if check():
        break

print(ans)