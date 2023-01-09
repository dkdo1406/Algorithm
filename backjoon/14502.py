import copy
import sys
from itertools import combinations
import collections



input = lambda : sys.stdin.readline()
copyGraph = []
N, M = map(int,input().split())
graph = []

def BFS(x, y):
    global copyGraph
    global N,M
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = collections.deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0<= ny < M and copyGraph[nx][ny] == 0:
                copyGraph[nx][ny]=2
                q.append((nx,ny))

for i in range(N):
    tmp_graph = list(map(int,input().split()))
    graph.append(tmp_graph)

# 0인 곳을 모두 입력한다.
safeZone = []
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j]==0:
            safeZone.append([i,j])
allSafeZone = list(combinations(safeZone,3))
maxcount = 0
# 벽세운거를 적용시키자
for k in allSafeZone:
    count = 0
    copyGraph = copy.deepcopy(graph)
    copyGraph[k[0][0]][k[0][1]] = 1
    copyGraph[k[1][0]][k[1][1]] = 1
    copyGraph[k[2][0]][k[2][1]] = 1

    for j in range(len(copyGraph)):
        for j2 in range(len(copyGraph[j])):
            if copyGraph[j][j2] == 2:
                BFS(j,j2)
    for i in range(len(copyGraph)):
        for i2 in range(len(copyGraph[i])):
            if copyGraph[i][i2]==0:
                count += 1
    maxcount = max(maxcount,count)

print(maxcount)





