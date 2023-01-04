import copy

N, M = list(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(N)]
cctv = []
cctv_5 = []
cctv_2 = []
cctv_else = []
visited = []
new_graph = [[0 for _ in range(M)] for _ in range(N)]
for r in range(N):
    for c in range(M):
        if graph[r][c] == 0 or graph[r][c] == 6:
            continue
        else:
            cctv.append([r, c])
        if graph[r][c] == 5:
            cctv_5.append([r, c])
        elif graph[r][c] == 2:
            cctv_2.append([r, c])
        else:
            cctv_else.append([r, c, graph[r][c]])
cctv_else.sort(key = lambda x: x[2], reverse= True)
cctv1 = [[(1,0)],[(-1,0)],[(0,1)],[(0,-1)]]
cctv2 = [[(1,0),(-1,0)],[(0,1),(0,-1)]]
cctv3 = [[(1,0),(0,-1)], [(1,0),(0,1)], [(-1, 0), (0, 1)], [(-1,0), (0,-1)]]
cctv4 = [[(1,0), (-1,0), (0,1)], [(1,0), (-1,0),(0,-1)], [(0,1),(0,-1),(1,0)], [(0,1),(0,-1),(-1,0)]]
cctv5 = [(1,0),(-1,0),(0,1),(0,-1)]

q = []
answer = 100
def checkBlank(new_graph):
    global answer
    cnt = 0
    for i in range(N):
        for j in range(M):
            if new_graph[i][j] == 0:
                cnt += 1
    answer = min(answer, cnt)

def DFS(L, new_graph):
    if L == len(cctv):
        checkBlank(new_graph)
        return
    r, c = cctv[L]

    if new_graph[r][c] == 5:
        temp_graph = copy.deepcopy(new_graph)
        for i in range(4):
            for j in range(1,9):
                nr = cctv5[i][0]*j + r
                nc = cctv5[i][1]*j + c
                if nr < 0 or nr >= N or nc < 0 or nc >= M or temp_graph[nr][nc] == 6:
                    break
                if temp_graph[nr][nc] == 0:
                    temp_graph[nr][nc] = '#'
                else:
                    continue
        DFS(L+1, temp_graph)
    if new_graph[r][c] == 4:
        for i in range(4):
            temp_graph = copy.deepcopy(new_graph)
            for j in range(3):
                for k in range(1, 9):
                    nr = cctv4[i][j][0]*k + r
                    nc = cctv4[i][j][1]*k + c
                    if nr < 0 or nr >= N or nc < 0 or nc >= M or temp_graph[nr][nc] == 6:
                        break
                    if temp_graph[nr][nc] == 0:
                        temp_graph[nr][nc] = '#'
                    else:
                        continue
            DFS(L+1, temp_graph)
    if new_graph[r][c] == 3:
        for i in range(4):
            temp_graph = copy.deepcopy(new_graph)
            for j in range(2):
                for k in range(1, 9):
                    nr = cctv3[i][j][0]*k + r
                    nc = cctv3[i][j][1]*k + c
                    if nr < 0 or nr >= N or nc < 0 or nc >= M or temp_graph[nr][nc] == 6:
                        break
                    if temp_graph[nr][nc] == 0:
                        temp_graph[nr][nc] = '#'
                    else:
                        continue
            DFS(L + 1, temp_graph)

    if new_graph[r][c] == 2:
        for i in range(2):
            temp_graph = copy.deepcopy(new_graph)
            for j in range(2):
                for k in range(1, 9):
                    nr = cctv2[i][j][0]*k + r
                    nc = cctv2[i][j][1]*k + c
                    if nr < 0 or nr >= N or nc < 0 or nc >= M or temp_graph[nr][nc] == 6:
                        break
                    if temp_graph[nr][nc] == 0:
                        temp_graph[nr][nc] = '#'
                    else:
                        continue
            DFS(L + 1, temp_graph)

    if new_graph[r][c] == 1:
        for i in range(4):
            temp_graph = copy.deepcopy(new_graph)
            for j in range(1):
                for k in range(1, 9):
                    nr = cctv1[i][j][0]*k + r
                    nc = cctv1[i][j][1]*k + c
                    if nr < 0 or nr >= N or nc < 0 or nc >= M or temp_graph[nr][nc] == 6:
                        break
                    if temp_graph[nr][nc] == 0:
                        temp_graph[nr][nc] = '#'
                    else:
                        continue
            DFS(L + 1, temp_graph)

DFS(0, graph)
print(answer)

