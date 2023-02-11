from collections import deque
from collections import defaultdict
N, M, K = list(map(int, input().split()))

magic = deque()
for i in range(M):
    r, c, m, s, d = list(map(int, input().split()))
    magic.append([r-1, c-1, m, s, d])

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(K):
    graph = [[defaultdict(int) for _ in range(N)] for _ in range(N)]
    while magic:
        r, c, m, s, d = magic.popleft()
        nr = r + dr[d] * s
        nc = c + dc[d] * s
        if nr >= N:
            nr = nr % N
        elif nr < 0:
            if -nr % N == 0:
                nr = 0
            else:
                nr = N - (-nr % N)
        if nc >= N:
            nc = nc % N
        elif nc < 0:
            if -nc % N == 0:
                nc = 0
            else:
                nc = N - (-nc % N)

        graph[nr][nc]['cnt'] += 1
        graph[nr][nc]['m'] += m
        graph[nr][nc]['s'] += s
        if graph[nr][nc]['cnt'] > 1:
            if graph[nr][nc]['d'] == -1:
                continue
            if d % 2 == 0 and graph[nr][nc]['d'] % 2 == 0:
                continue
            if d % 2 != 0 and graph[nr][nc]['d'] % 2 != 0:
                continue
            graph[nr][nc]['d'] = -1
        else:
            graph[nr][nc]['d'] = d
    ans = 0
    for r in range(N):
        for c in range(N):
            if graph[r][c] and graph[r][c]['cnt'] > 1:
                cnt = graph[r][c]['cnt']
                m = graph[r][c]['m'] // 5
                s = graph[r][c]['s'] // cnt
                if graph[r][c]['d'] == -1:
                    d = [1, 3, 5, 7]
                else:
                    d = [0, 2, 4, 6]
                if m == 0:
                    continue
                for i in d:
                    magic.append([r, c, m, s, i])
                    ans += m
            elif graph[r][c] and graph[r][c]['cnt'] == 1:
                ans += graph[r][c]['m']
                magic.append([r, c, graph[r][c]['m'], graph[r][c]['s'], graph[r][c]['d']])
print(ans)