from collections import deque
from collections import defaultdict
import copy
M, S = list(map(int, input().split()))
graph = [[0 for _ in range(5)] for _ in range(5)]
fish = deque()
fish_graph = [[defaultdict(int) for _ in range(5)] for _ in range(5)]
for i in range(M):
    r, c, direct = list(map(int, input().split()))
    fish.append([r, c, direct])
    graph[r][c] += 1
r,c = list(map(int, input().split()))
blood_graph = [[0 for _ in range(5)] for _ in range(5)]
shark = [r, c]

fish_dic = [[defaultdict(int) for _ in range(5)] for _ in range(5)]
for r, c, d in fish:
    fish_graph[r][c][d] += 1

def copyMagic():
    global fish_dic, fish_graph
    fish_dic = copy.deepcopy(fish_graph)

def magic():
    global fish_dic, fish_graph
    for r in range(5):
        for c in range(5):
            for key, value in fish_dic[r][c].items():
                fish_graph[r][c][key] += value
                graph[r][c] += value

def move():
    global fish_graph
    dr = [0, 0, -1, -1, -1, 0, 1, 1, 1]
    dc = [0, -1, -1, 0, 1, 1, 1, 0, -1]
    fish_graph = [[defaultdict(int) for _ in range(5)] for _ in range(5)]
    for r in range(1,5):
        for c in range(1,5):
            if fish_dic[r][c]:
                for dir, cnt in fish_dic[r][c].items():
                    fish_graph[r][c][dir] += cnt
                    origin_dir = dir
                    for _ in range(9):
                        if dir == 0:
                            dir = 8
                        nr = r + dr[dir]
                        nc = c + dc[dir]
                        if nr < 1 or nr > 4 or nc < 1 or nc > 4 or [nr, nc] == shark or blood_graph[nr][nc] != 0:
                            dir -= 1
                            continue
                        fish_graph[nr][nc][dir] += cnt
                        fish_graph[r][c][origin_dir] -= cnt
                        if fish_graph[r][c][origin_dir] == 0:
                            fish_graph[r][c].pop(origin_dir)
                        graph[nr][nc] += cnt
                        graph[r][c] -= cnt
                        break

def bite(L, r, c, res, pri, new_graph):
    global ans
    if L == -1:
        if ans[0] < res:
            ans = [res, pri]
        elif ans[0] == res and ans[1] > pri:
            ans = [res, pri]
        return
    dr = [0, -1, 0, 1, 0]
    dc = [0, 0, -1, 0, 1]
    for i in range(1, 5):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 1 or nr > 4 or nc < 1 or nc > 4:
            continue
        copy_graph = copy.deepcopy(new_graph)
        score = copy_graph[nr][nc]
        copy_graph[nr][nc] = 0

        bite(L - 1, nr, nc, res + score, pri + (i * (10 ** L)), copy_graph)

def move_shark(ans):
    global shark
    dr = [0, -1, 0, 1, 0]
    dc = [0, 0, -1, 0, 1]
    r, c = shark
    for s in str(ans):
        r += dr[int(s)]
        c += dc[int(s)]
        if graph[r][c] > 0:
            graph[r][c] = 0
            blood_graph[r][c] = 3
            fish_graph[r][c] = defaultdict(int)
        else:
            continue
    shark = [r, c]


def removeBlood():
    for r in range(1, 5):
        for c in range(1, 5):
            if blood_graph[r][c] != 0:
                blood_graph[r][c] -= 1


for _ in range(S):

    copyMagic()
    move()

    ans = [0, 555]
    new_graph = copy.deepcopy(graph)
    bite(2, shark[0], shark[1], 0, 0, new_graph)

    move_shark(ans[1])
    removeBlood()
    magic()


ans = 0
for i in graph:
    ans += sum(i)
print(ans)
