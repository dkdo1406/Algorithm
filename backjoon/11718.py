import sys
input = lambda: sys.stdin.readline()
R,C,T = map(int,input().split())
graph = []
totalGraph = [[0] * C for i in range(R)]

def san(graph,x,y):
    print(graph[x][y])
    global R,C
    tempGraph = [[0] * C for i in range(R)]
    dx = [1, -1 ,0, 0]
    dy = [0, 0, 1, -1]

    # print(tempgraph)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= C or nx < 0 or ny >= R or ny < 0:
            continue

    return tempGraph

for i in range(R):
    graph.append(list(map(int,input().split())))

for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] != 0 and graph[i][j] != -1:
            san(graph,i,j)




