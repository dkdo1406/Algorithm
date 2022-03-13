"""
1번 정점에서 각 정점으로 가는 최소 이동 간선 수

"""
import collections

N,M = map(int,input().split())
graph = [[] for i in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
visited = [-1]*(N+1)
level = [[] for i in range(20)]

def BFS(n,graph):
    q = collections.deque()
    q.append(n)
    visited[n] = 0
    while q:
        V = q.popleft()
        for i in graph[V]:
            if visited[i]:
                visited[i] = visited[V]+1
                q.append(i)
def BFS_level(n,graph):
    q = collections.deque()
    q.append(n)
    visit = [False]*(N+1)
    visit[n]=True
    L = 0
    level[L].append(n)
    while q:
        L+=1
        for i in range(len(q)):
            V = q.popleft()
            for i in graph[V]:
                if not visit[i]:
                    visit[i] = True
                    level[L].append(i)
                    q.append(i)

BFS(1,graph)
for i in range(2,N+1):
    print(i,':',visited[i])
print()
print()

BFS_level(1,graph)
for i,level in enumerate(level):
    if level:
        print(i,":",level)


