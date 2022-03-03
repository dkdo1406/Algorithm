"""
입력
첫째줄에 정점N, 간선 M, 시작번호 V
다음줄 부터 M개의 간선 정보
출력
첫째줄 DFS, 둘째줄 BFS
"""
import sys
input = lambda : sys.stdin.readline()
from collections import deque


N,M,V = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    i,j = map(int,input().split())
    graph[i].append(j)
    graph[j].append(i)
graph = [sorted(i) for i in graph]
visited = [False]*(N+1)
def DFS(start,graph,visited):

    visited[start] = True
    print(start,end=' ')
    for i in graph[start]:
        if not visited[i]:
            DFS(i,graph,visited)

def BFS(start,graph,visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
DFS(V,graph,visited)
print('')             
visited = [False]*(N+1)
BFS(V,graph,visited)