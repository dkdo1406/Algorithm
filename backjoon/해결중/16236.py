from collections import deque
N = int(input())
graph = [list(map(int,input().split())) for i in range(N)]
shark = []
result = 0
lv = 2
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == 9:
            shark.append([i,j])
def bfs(count,x,y):
    global N, graph,lv
    graph[x][y] = 0
    # dx = [1,-1,0,0]
    # dy = [0,0,1,-1]
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    q = deque()
    q.append((count,x,y))

    canEat = []
    visited = [[x,y]]
    while q:
        count, x, y = q.popleft()
        for i in range(4):
            nx = x + dy[i]
            ny = y + dx[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] > lv:
                continue
            if graph[nx][ny] == lv or graph[nx][ny] == 0:
                if [nx,ny] not in visited:
                    visited.append([nx, ny])
                    q.append((count + 1, nx, ny))
            if graph[nx][ny] < lv:
                if [nx, ny] not in visited:
                    visited.append([nx, ny])
                    canEat.append([count, nx,ny])
    canEat.sort(key = lambda x : (x[0],x[1],x[2])) # 거리 위 왼쪽 순
    if len(canEat) == 0:
        return False
    return canEat[0]
result = 0

newY = shark[0][0]
newX =  shark[0][1]
cnt = 0
while True:

    newbfs = bfs(1, newY, newX)
    if newbfs is False:
        break
    result += newbfs[0]
    newY = newbfs[1]
    newX = newbfs[2]
    cnt += 1
    if cnt == lv:
        lv += 1
        cnt = 0
print(result)







#
# fishes = deque() # 물고기 위치
# shark = [] # 상어 위치
# cant = deque()
# dx = [0,1,0,-1]
# dy = [-1,0,1,0]
# for i in range(len(graph)):
#     for j in range(len(graph[i])):
#         if graph[i][j] == 9:
#             shark.append([i,j,graph[i][j]])
#         elif graph[i][j] != 9 and graph[i][j] != 0 and graph[i][j] == 2:
#             fishes.append([i,j,graph[i][j]])
#         elif graph[i][j] != 9 and graph[i][j] != 0 and graph[i][j] > 2:
#             cant.append([i,j,graph[i][j]])
#
# print(fishes)
# cant = sorted(cant, key= lambda x: x[2])
# print(cant)
# exit()
# # def move(shark):
# # 물고기 정렬 (상어에 가까우면서 상어보다 크기 작은 순서대로)
# # 상어 이동
# # def fishSort(fishes, shark):
# #     for i,j, fishes:
# #         pass
#
# if len(fishes) == 0:
#     print(0)
# else:
#     fishSort(fishes,shark)
#
#
#
#
# print(fishes)
# print(shark)
