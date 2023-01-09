import copy

n, m = list(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(n)]

cctv = []
for r in range(n):
    for c in range(m):
        if 0 < graph[r][c] < 6:
            cctv.append([r, c])
answer = 65
cctv1 = [[1,0],[-1,0],[0,1],[0,-1]]
cctv5 = [[1,0],[-1,0],[0,1],[0,-1]]
cctv2 = [[[1,0],[-1,0]],[[0,1],[0,-1]]]
cctv3 = [[[-1,0],[0,1]], [[0,1],[1,0]], [[1,0],[0,-1]], [[0,-1],[-1,0]]]
cctv4 = [[[-1,0],[0,-1],[1,0]], [[0,-1],[1,0],[0,1]], [[1,0],[0,1],[-1,0]], [[0,1],[-1,0],[0,-1]]]

def DFS(L, graph):
    global answer
    if L == len(cctv):
        cnt = 0
        for r in range(n):
            for c in range(m):
                if graph[r][c] == 0:
                    cnt += 1
        answer = min(answer, cnt)
        return
    r, c = cctv[L]
    if graph[r][c] == 1:
        for i in cctv1:
            new_graph = copy.deepcopy(graph)
            for idx in range(1,9):
                nr = r + i[0]*idx
                nc = c + i[1]*idx
                if nr < 0 or nr >= n or nc < 0 or nc >= m or new_graph[nr][nc] == 6:
                    break
                if new_graph[nr][nc] == 0:
                    new_graph[nr][nc] = '#'
            DFS(L+1, new_graph)

    elif graph[r][c] == 2:
        for i in cctv2:
            new_graph = copy.deepcopy(graph)
            for j in i:
                for idx in range(1, 9):
                    nr = r + j[0]*idx
                    nc = c + j[1]*idx
                    if nr < 0 or nr >= n or nc < 0 or nc >= m or new_graph[nr][nc] == 6:
                        break
                    if new_graph[nr][nc] == 0:
                        new_graph[nr][nc] = '#'
            DFS(L + 1, new_graph)

    elif graph[r][c] == 3:
        for i in cctv3:
            new_graph = copy.deepcopy(graph)
            for j in i:
                for idx in range(1, 9):
                    nr = r + j[0] * idx
                    nc = c + j[1] * idx
                    if nr < 0 or nr >= n or nc < 0 or nc >= m or new_graph[nr][nc] == 6:
                        break
                    if new_graph[nr][nc] == 0:
                        new_graph[nr][nc] = '#'
            DFS(L + 1, new_graph)

    elif graph[r][c] == 4:
        for i in cctv4:
            new_graph = copy.deepcopy(graph)
            for j in i:
                for idx in range(1, 9):
                    nr = r + j[0] * idx
                    nc = c + j[1] * idx
                    if nr < 0 or nr >= n or nc < 0 or nc >= m or new_graph[nr][nc] == 6:
                        break
                    if new_graph[nr][nc] == 0:
                        new_graph[nr][nc] = '#'
            DFS(L + 1, new_graph)
    elif graph[r][c] == 5:
        new_graph = copy.deepcopy(graph)
        for i in cctv5:
            for idx in range(1,9):
                nr = r + i[0]*idx
                nc = c + i[1]*idx
                if nr < 0 or nr >= n or nc < 0 or nc >= m or new_graph[nr][nc] == 6:
                    break
                if new_graph[nr][nc] == 0:
                    new_graph[nr][nc] = '#'
        DFS(L+1, new_graph)


DFS(0, graph)
print(answer)
