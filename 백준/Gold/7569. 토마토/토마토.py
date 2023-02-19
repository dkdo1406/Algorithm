from collections import deque
M, N, H = list(map(int, input().split()))
graph = [[] for _ in range(H)]
for i in range(H):
    graph[i] = [list(map(int, input().split())) for _ in range(N)]

def searchPotato():
    tomato = deque()
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if graph[h][r][c] > 0:
                    tomato.append((h,r,c))
    spread(tomato)


def spread(tomato):
    while tomato:
        h, r, c = tomato.popleft()
        dr = [1, -1, 0, 0, 0, 0]
        dc = [0, 0, -1, 1, 0, 0]
        dh = [0, 0, 0, 0, -1, 1]
        for i in range(6):
            nr = r + dr[i]
            nc = c + dc[i]
            nh = h + dh[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= M or nh < 0 or nh >= H or graph[nh][nr][nc] == -1 or graph[nh][nr][nc] == 1:
                continue
            if graph[nh][nr][nc] == 0:
                graph[nh][nr][nc] = graph[h][r][c] + 1
                tomato.append((nh, nr, nc))
            elif graph[h][r][c] + 1 < graph[nh][nr][nc]:
                graph[nh][nr][nc] = graph[h][r][c] + 1
                tomato.append((nh, nr, nc))

searchPotato()

def check():
    ans = 0
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if graph[h][r][c] == 0:
                    return -1
                ans = max(ans, graph[h][r][c])
    return ans - 1
print(check())