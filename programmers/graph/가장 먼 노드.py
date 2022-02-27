"""
문제 : https://programmers.co.kr/learn/courses/30/lessons/49189?language=python3
처음에는 단방향으로 코드를 짜서 테스트케이스 3만 통과함

양방향이라 정렬할 필요없고
edge = sorted([sorted(x) for x in edge])
이렇게 하면 단방향이라 최대값을 구하지 못한다.
[graph[i[0]].append(i[1]) for i in edge] 

n=6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	
"""
from collections import deque

n = 4
edge = 	[[1, 4], [4, 3], [1, 2]]
graph= [[] for i in range(n+1)]

for i, j in edge:
    graph[i].append(j)
    graph[j].append(i)
print(graph)
answer =0
visited = [False] * (n+1)
distances = [0] *(n+1)
print(visited)

def bfs(start,graph,visited):
    queue = deque([start])
    visited[start] = True
    distances[start] = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
                distances[i] = distances[v] +1


bfs(1,graph,visited)
print(graph)
print(visited)
print(distances)
print('정답은?',distances.count(max(distances)))