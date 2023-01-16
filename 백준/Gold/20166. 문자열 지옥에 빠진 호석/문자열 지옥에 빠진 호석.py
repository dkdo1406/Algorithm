from collections import deque
from collections import defaultdict
n, m, k = list(map(int, input().split()))

graph = [list(input()) for _ in range(n)]

god = [input() for _ in range(k)]

dr = [1,-1,0,0,1,1,-1,-1]
dc = [0,0,1,-1,1,-1,1,-1]

dic = defaultdict(int)
def BFS(r, c):
    q = deque()
    q.append((r, c, graph[r][c]))
    while q:
        r, c, godDid = q.popleft()
        if len(godDid) == 5:
            dic[godDid] += 1
            continue
        for i in range(8):
            nr = dr[i] + r
            nc = dc[i] + c
            if nr < 0:
                nr = n-1
            if nc < 0:
                nc = m-1
            if nr == n:
                nr = 0
            if nc == m:
                nc = 0
            q.append((nr, nc, godDid + graph[nr][nc]))

for r in range(n):
    for c in range(m):
        BFS(r, c)
for did in god:
    print(dic[did])