from collections import deque
from collections import defaultdict
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

new_graph = defaultdict(list)
for i in range(N):
    new_graph[i] = []
    for j in range(N):
        if graph[i][j] == 1:
            new_graph[i].append(j)

def bfs(node, s):
    q = deque()
    q.append(s)
    while q:
        s = q.popleft()
        for n in s:
            if n in visited:
                continue
            if not new_graph[n]:
                visited.add(n)
                graph[node][n] = 1
                continue
            visited.add(n)
            q.append(new_graph[n])
            graph[node][n] = 1

visited = set()
for i, j in new_graph.items():
    visited = set()
    bfs(i, j)
for i in graph:
    for j in i:
        print(j, end = ' ')
    print()