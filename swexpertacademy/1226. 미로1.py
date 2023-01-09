from collections import deque

T = 10

def bfs():
    global graph
    q = deque()
    q.append((1,1))
    visited = []
    visited.append((1,1))
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dy[i]
            ny = y + dx[i]
            if nx < 1 or nx >= 15 or ny < 1 or ny >= 15:
                continue
            if graph[nx][ny] == 1 or graph[nx][ny] == 2:
                continue
            if graph[nx][ny] == 3:
                return 1
            graph[nx][ny] = 2
            q.append((nx,ny))
    return 0
for test_case in range(1, 11):
    N = int(input())
    graph = [list(map(int, input())) for _ in range(16)]
    answer = bfs()
    for i in graph:
        print(i)
    print("#{0} {1}".format(N, answer))
