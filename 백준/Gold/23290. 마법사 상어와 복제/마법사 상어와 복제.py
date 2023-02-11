import copy
from collections import defaultdict
from collections import deque
M, S = list(map(int, input().split()))

fish_dic = [[defaultdict(int) for _ in range(4)] for _ in range(4)]
graph_dic = [[defaultdict(int) for _ in range(4)] for _ in range(4)]
graph = [[0 for _ in range(4)] for _ in range(4)]
blood_graph = [[0 for _ in range(4)] for _ in range(4)]
for i in range(M):
    r, c, dir = list(map(int, input().split()))
    graph_dic[r-1][c-1][dir-1] += 1
    graph[r-1][c-1] += 1

r, c = list(map(int, input().split()))
shark = [r-1, c-1]

def copyMagic():
    global fish_dic
    fish_dic = copy.deepcopy(graph_dic)

def magic():
    global graph_dic, graph
    for r in range(4):
        for c in range(4):
            if fish_dic[r][c]:
                for dir, count in fish_dic[r][c].items():
                    graph_dic[r][c][dir] += count
                    graph[r][c] += count
def moveFish():
    global graph_dic
    graph_dic = [[defaultdict(int) for _ in range(4)] for _ in range(4)]
    "←, ↖, ↑, ↗, →, ↘, ↓, ↙ "
    dr = [0, -1, -1, -1, 0, 1, 1, 1]
    dc = [-1, -1, 0, 1, 1, 1, 0, -1]
    for r in range(4):
        for c in range(4):
            if fish_dic[r][c]:
                for dir, cnt in fish_dic[r][c].items():
                    before_dir = dir
                    graph_dic[r][c][before_dir] += cnt
                    for _ in range(9):
                        if dir == -1:
                            dir = 7
                        nr = r + dr[dir]
                        nc = c + dc[dir]
                        if nr < 0 or nr >= 4 or nc < 0 or nc >= 4 or [nr, nc] == shark or blood_graph[nr][nc] != 0:
                            dir -= 1
                            continue
                        graph_dic[nr][nc][dir] += cnt
                        graph_dic[r][c][before_dir] -= cnt
                        if graph_dic[r][c][before_dir] == 0:
                            graph_dic[r][c].pop(before_dir)
                        graph[nr][nc] += cnt
                        graph[r][c] -= cnt
                        break

def findFish():
    global shark
    r, c = shark
    dr = [-1,0,1,0]
    dc = [0,-1,0,1]
    q = deque()
    copy1 = copy.deepcopy(graph)
    q.append((r, c, [], 0, copy1))
    ans = [9, 9, 9]
    ans_sum = 0
    while q:
        r, c, dir, res, graph1 = q.popleft()
        if len(dir) == 3:
            if res > ans_sum:
                ans_sum = res
                ans = dir
            elif ans_sum == res and ans > dir:
                ans = dir
        else:
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if nr < 0 or nr >= 4 or nc < 0 or nc >= 4:
                    continue
                copy_graph = copy.deepcopy(graph1)
                score = copy_graph[nr][nc]
                copy_graph[nr][nc] = 0
                q.append((nr, nc, dir + [i], res + score, copy_graph))
    r, c = shark
    for i in ans:
        r += dr[i]
        c += dc[i]
        if graph[r][c] != 0:
            graph[r][c] = 0
            graph_dic[r][c] = defaultdict(int)
            blood_graph[r][c] = 3
    shark = [r, c]

def blood():
    for r in range(4):
        for c in range(4):
            if blood_graph[r][c] != 0:
                blood_graph[r][c] -= 1

for _ in range(S):
    copyMagic()
    moveFish()
    findFish()
    blood()
    magic()
ans = 0
for i in graph:
    ans += sum(i)
print(ans)
