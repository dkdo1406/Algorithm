import copy
from collections import deque
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, W, H = list(map(int, input().split()))
    graph = []
    for _ in range(H):
        graph.append(list(map(int, input().split())))
    ans = W * H * 10

    def shoot(r, c, new_graph):
        dr = [0,0,-1,1]
        dc = [1,-1,0,0]
        q = deque()
        q.append((r, c, new_graph[r][c]))
        if new_graph[r][c] == 1:
            new_graph[r][c] = 0
            return new_graph
        while q:
            r, c, num = q.popleft()
            for i in range(4):
                for s in range(num):
                    nr = dr[i] * s + r
                    nc = dc[i] * s + c
                    if nr < 0 or nr >= H or nc < 0 or nc >= W:
                        break
                    if new_graph[nr][nc] > 1:
                        q.append((nr, nc, new_graph[nr][nc]))
                    new_graph[nr][nc] = 0
        return new_graph

    def move(new_graph):
        for c in range(W):
            r = H - 1
            while r >= 0:
                if new_graph[r][c] == 0:
                    u = r - 1
                    while u >= 0:
                        if new_graph[u][c] > 0:
                            new_graph[r][c], new_graph[u][c] = new_graph[u][c], new_graph[r][c]
                            break
                        u -= 1
                r -= 1
        return new_graph

    def DFS(L, new_graph):
        global ans
        if L == N:
            res = 0
            for c in range(W):
                for r in range(H-1, -1, -1):
                    if new_graph[r][c] > 0:
                        res += 1
                    else:
                        break
            ans = min(ans, res)
            return

        for c in range(W):
            for r in range(H):
                if new_graph[r][c] > 0:
                    copy_graph = copy.deepcopy(new_graph)
                    copy_graph = shoot(r, c, copy_graph)
                    copy_graph = move(copy_graph)
                    DFS(L+1, copy_graph)
                    break
        DFS(L+1, new_graph)

    DFS(0, graph)


    print(f"#{test_case} {ans}")