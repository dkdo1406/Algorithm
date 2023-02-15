import copy
from collections import deque
N, Q = list(map(int, input().split()))
N = 2 ** N
graph = [list(map(int, input().split())) for _ in range(N)]
arr = list(map(int, input().split()))

def spin(L):
    global graph
    L = 2 ** L
    new_graph = [[0 for _ in range(N)] for _ in range(N)]
    r_cnt = 0
    c_cnt = 0
    while r_cnt < N:
        n_c = c_cnt
        for r in range(r_cnt, r_cnt + L):
            n_r = r_cnt + L - 1
            for c in range(c_cnt, c_cnt + L):
                new_graph[r][c] = graph[n_r][n_c]
                n_r -= 1
            n_c += 1
        c_cnt += L
        if c_cnt == N:
            c_cnt = 0
            r_cnt += L
    graph = new_graph
def checkIce():
    global graph
    new_graph = [[0 for _ in range(N)] for _ in range(N)]
    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]
    q = deque()
    q.append([0, 0])

    for r in range(N):
        for c in range(N):
            if graph[r][c] == 0:
                new_graph[r][c] = graph[r][c]
            else:
                cnt = 0
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if nr < 0 or nr >= N or nc < 0 or nc >= N or graph[nr][nc] == 0:
                        continue
                    cnt += 1
                if cnt < 3:
                    new_graph[r][c] = graph[r][c] - 1
                else:
                    new_graph[r][c] = graph[r][c]
    graph = new_graph

for L in arr:
    spin(L)
    checkIce()
sum_ans = 0
not_zero_ans = 0

def countIce(r, c):
    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]
    ans = 0
    q = deque()
    q.append((r, c))
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N or graph[nr][nc] == 0:
                continue
            ans += 1
            graph[nr][nc] = 0
            q.append((nr, nc))
    return ans

for i in graph:
    sum_ans += sum(i)
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            not_zero_ans = max(not_zero_ans, countIce(i, j))

print(sum_ans)
print(not_zero_ans)

