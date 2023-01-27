import sys
from collections import deque
input = lambda : sys.stdin.readline()

H, W = list(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(H)]
Q = int(input())
change = [list(map(int, input().split())) for _ in range(Q)]

dr = [1,-1,0,0]
dc = [0,0,-1,1]

def BFS(i,j,p):
    q = deque()
    q.append([i,j])
    start = graph[i][j]
    graph[i][j] = p
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c
            if nr < 0 or nr >= H or nc < 0 or nc >= W or graph[nr][nc] != start:
                continue
            graph[nr][nc] = p
            q.append([nr, nc])

for i,j,c in change:
    if graph[i-1][j-1] != c:
        BFS(i-1,j-1,c)
for i in graph:
    for j in i:
        print(j, end= ' ')
    print()