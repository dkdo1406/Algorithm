import copy
from collections import deque

N, M = list(map(int,input().split()))
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs(x,y):
    global graph, dx, dy, N, globalVisited
    rainbowCount = 0
    count = 1
    q = deque()
    q.append((x,y))
    visited = []
    visited.append((x,y))
    value = graph[x][y]
    while q:
        x2,y2 = q.popleft()
        for i in range(4):
            nx = x2 + dy[i]
            ny = y2 + dx[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == -1:
                continue
            elif graph[nx][ny] == 0:
                if (nx, ny) not in visited:
                    rainbowCount += 1
                    count += 1
                    q.append((nx,ny))
                    visited.append((nx,ny))
            elif value == graph[nx][ny]:
                if (nx, ny) not in visited:
                    count +=1
                    q.append((nx, ny))
                    visited.append((nx, ny))
                    globalVisited[nx][ny] = True
    return count, rainbowCount, x, y
def dropDown():
    global graph, N

    while True:
        newGraph = copy.deepcopy(graph)
        for R in range(N-1, 0, -1):
            for C in range(N):
                if graph[R][C] == -1:
                    continue
                if graph[R-1][C] == -1:
                    continue
                if graph[R][C] == []:
                    graph[R][C], graph[R-1][C] = graph[R-1][C], graph[R][C]
        if graph == newGraph:
            break

score = 0


def delete(list):
    global graph, dx, dy, N
    _,_,x,y = list
    value = graph[x][y]
    graph[x][y] = []

    q = deque()
    q.append((x,y))
    visited = []
    visited.append((x,y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dy[i]
            ny = y + dx[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == -1:
                continue

            if graph[nx][ny] == value or graph[nx][ny] == 0:
                if (nx,ny) not in visited:
                    graph[nx][ny] = []
                    q.append((nx,ny))
                    visited.append((nx,ny))


def rotate():
    global graph, N
    newGraph = copy.deepcopy(graph)
    for R in range(N):
        for C in range(N):
            newGraph[R][C] = graph[C][N-1-R]
    graph = newGraph
count = 0
while True:
    globalVisited = [[False for i in range(N)] for i in range(N)]
    count +=1
    list = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 0 or graph[i][j] == -1 or graph[i][j] == []:
                globalVisited[i][j] = True
                continue

            if not globalVisited[i][j]:
                globalVisited[i][j] = True
                result = bfs(i,j)

            if result[0] != 1 and result[0] != []:
                list.append(result)

    list.sort(key= lambda x: (-x[0], -x[1], -x[2], -x[3]))
    if len(list) == 0:

        break
    score += list[0][0] ** 2
    delete(list[0])

    dropDown()
    rotate()
    dropDown()

print(score)

