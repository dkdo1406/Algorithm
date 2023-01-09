N,M = map(int,input().split())
graph = []
move = []
for i in range(N):
    graph.append(list(map(int,input().split())))
for i in range(M):
    move.append(list(map(int,input().split())))

cloud = [(N-1,0),(N-1,1),(N-2,0),(N-2,1)]

def cloud_move(direction, count):
    global cloud
    tmpCloud = []
    for i in cloud:
        if direction == 1:
            x = ((i[1] + N * 50) - count) % N
            y = i[0]
        elif direction == 2:
            x = ((i[1] + N * 50) - count) % N
            y = ((i[0] + N * 50) - count) % N
        elif direction == 3:
            x = i[1]
            y = ((i[0] + N * 50) - count) % N
        elif direction == 4:
            x = ((i[1] + N * 50) + count) % N
            y = ((i[0] + N * 50) - count) % N
        elif direction == 5:
            x = ((i[1] + N * 50) + count) % N
            y = i[0]
        elif direction == 6:
            x = ((i[1] + N * 50) + count) % N
            y = ((i[0] + N * 50) + count) % N
        elif direction == 7:
            x = i[1]
            y = ((i[0] + N * 50) + count) % N
        elif direction == 8:
            x = ((i[1] + N * 50) - count) % N
            y = ((i[0] + N * 50) + count) % N
        tmpCloud.append((y,x))
    cloud = tmpCloud


def addWater(graph):
    global cloud
    for x,y in cloud:
        graph[x][y] += 1
    return graph


def water_bug():
    global cloud, N, graph
    dx = [-1, -1, 1, 1]
    dy = [1, -1, -1, 1]
    for i in cloud:
        cnt = 0
        for j in range(4):
            nx = i[1] + dx[j]
            ny = i[0] + dy[j]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[ny][nx] == 0:
                continue
            cnt += 1
        graph[i[0]][i[1]] += cnt


def makeCloud():
    global cloud, graph
    tmpCloud = []
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] >= 2 and (i,j) not in cloud:
                tmpCloud.append((i,j))
                graph[i][j] -= 2
    cloud = tmpCloud

for i in move:
    cloud_move(i[0],i[1])
    graph = addWater(graph)
    water_bug()
    makeCloud()
answer = 0
for i in graph:
    answer += sum(i)
print(answer)
