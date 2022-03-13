"""
1에서 시작, 1이 감염시킨 PC대수를 구하라

7
6
1 2
2 3
1 5
5 2
5 6
4 7
"""
import sys
import collections
N = int(input())
T = int(input())
graph = [[] for i in range(N+1)]
visited = [False]*(N+1)
for i in range(T):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
q = collections.deque()

def bfs(start,graph,visited):
    q.append(start)
    visited[start]=True
    while q:
        abc = q.popleft()
        for i in graph[abc]:
            if not visited[i]:
                visited[i]=True
                q.append(i)

bfs(1,graph,visited)
print(visited.count(True)-1)
