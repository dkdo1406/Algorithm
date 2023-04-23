import collections

R, C, M = list(map(int, input().split()))

ans = 0
shark = collections.deque()
graph = [[[] for _ in range(C)] for _ in range(R)]

dr = [-1,1,0,0]
dc = [0,0,1,-1]
for _ in range(M):
    r, c, s, d, z = list(map(int, input().split()))

    if d < 3:
        check = (R - 1) * 2
    else:
        check = (C - 1) * 2
    shark.append([r-1, c-1, s % check, d-1, z])
    graph[r-1][c-1] = [s % check, d-1, z]

def fishing(index):
    global ans
    for r in range(R):
        if graph[r][index]:
            ans += graph[r][index][2]
            graph[r][index].clear()
            break

def move_shark():
    global graph
    copy_graph = [[[] for _ in range(C)] for _ in range(R)]
    for _ in range(len(shark)):
        r, c, s, d, z = shark.popleft()
        if graph[r][c] != [s, d, z]:
            continue

        nr = r + dr[d] * s
        nc = c + dc[d] * s

        while nr < 0 or nr >= R or nc < 0 or nc >= C:
            if nr < 0:
                nr = abs(nr)
                d = 1
            elif nc < 0:
                nc = abs(nc)
                d = 2
            elif nr >= R:
                nr = (R - 1) - (nr - (R - 1))
                d = 0

            elif nc >= C:
                nc = (C - 1) - (nc - (C - 1))
                d = 3

        if copy_graph[nr][nc]:
            if z < copy_graph[nr][nc][2]:
                continue
        copy_graph[nr][nc] = [s,d,z]
        shark.append([nr, nc, s, d, z])

    graph = copy_graph

for i in range(C):
    fishing(i)
    move_shark()

print(ans)