import copy
from collections import deque
# bfs 예제
N = 6

graph = [[1e10 for _ in range(N)] for _ in range(N)]
newGraph = copy.deepcopy(graph)
answer = 100000000001
for i in range(N):
    a = list(input())
    for index,k in enumerate(a):
        graph[i][index] = int(k)
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]
# graph = [list(map(string,input().split())) for i in range(N)]

for i in graph:
    print(i)
def dfs(x,y, visited, result):
    global graph, answer, dx, dy

    if x == N-1 and y == N-1:
        answer = min(result, answer)
        return
    for i in range(4):
        nx = x + dy[i]
        ny = y + dx[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if (nx,ny) not in visited:
            visited.append((nx,ny))
            #한개는 방문하는것 한개는 방문안하고 다른곳 가는 경우
            dfs(nx,ny,visited, result + graph[nx][ny])


def recover():
    global graph, dx, dy, N, newGraph
    x, y = 0, 0
    q = deque()
    q.append((x,y))
    newGraph[x][y] = 0
    while q:
        newX, newY = q.popleft()
        for i in range(4):
            nx = newX + dy[i]
            ny = newY + dx[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if newGraph[nx][ny] > graph[nx][ny] + newGraph[newX][newY]:
                newGraph[nx][ny] = graph[nx][ny] + newGraph[newX][newY]
                q.append((nx, ny))
        for a in newGraph:
            print(a)

    # return reallyGo[0][2]
recover()
print(newGraph[N - 1][N - 1])
# dfs(0,0,[(0,0)],0)
# print(answer)
for i in newGraph:
    print(i)