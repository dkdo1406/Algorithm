import copy

arr = [list(map(int, input().split())) for _ in range(4)]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

graph = [[[] for _ in range(4)] for _ in range(4)]

for i in range(4):
    cnt = 0
    for j in range(0, 8, 2):
        graph[i][cnt] = arr[i][j:j+2]
        cnt+=1

answer = graph[0][0][0]
graph[0][0][0] = 50

#도망가는 코드
def move():
    global dx, dy
    for fish in range(1,17):
        x, y, dir = -1, -1, -1
        for R in range(4):
            for C in range(4):
                if graph[R][C][0] == fish:
                    x, y, dir = R, C, graph[R][C][1]
                    locate = graph[R][C][1]
        if dir == -1:
            continue
        for i in range(8):
            fdir = (dir - 1 + i) % 8
        # for i in range(dir - 1, dir + 7):
            nx = x + dy[fdir]
            ny = y + dx[fdir]
            if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
                continue
            if graph[nx][ny][0] == 50:
                continue
            graph[x][y][1] = fdir+1
            graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
            break

def sharkMove(sx, sy, sdir, eat):
    global answer, graph
    move()
    redo = copy.deepcopy(graph)

    caneat = []
    for cnt in range(1, 4):
        nx = sx + dy[sdir - 1] * cnt
        ny = sy + dx[sdir - 1] * cnt
        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4 or graph[nx][ny][0] == 0:
            continue
        caneat.append([graph[nx][ny][0], nx, ny])
    if not caneat:
        answer = max(answer, eat)
        return
    for num, x, y, in caneat:
        graph = copy.deepcopy(redo)
        graph[x][y][0] = 50
        graph[sx][sy][0] = 0
        sharkMove(x,y,graph[x][y][1], eat + num)


sharkMove(0, 0, graph[0][0][1], answer)
print(answer)






