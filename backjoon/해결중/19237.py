N,M,K = list(map(int, input().split()))
K +=1
graph = [[] for i in range(N)]
pheromone = [[[] for _ in range(N)] for _ in range(N)]
for i in range(N):
    a = list(map(int,input().split()))
    for j in range(N):
        graph[i].append([a[j]])

dx = [0, 0, 0, -1, 1]
dy = [0, -1, 1, 0, 0]
sharkD = list(map(int, input().split()))
for i in range(len(graph)):
    for j in range(len(graph[i])):
        for index, l in enumerate(sharkD):
            if graph[i][j][0] == index + 1:
                graph[i][j].append(l)
                pheromone[i][j] = [index + 1, K, 1]

sharkMove = [[] for _ in range(M)]
for i in range(M):
    for j in range(4):
        sharkMove[i].append(list(map(int, input().split())))

# 순서 1. 상어의 이동 2.페로몬 줄이기 3. 페로몬 뿌리기 4. 1혼자 남았는지 체크

def move(num,x,y,d):
    global N,K, graph, pheromone
    dx = [0, 0, 0, -1, 1]
    dy = [0, -1, 1, 0, 0]
    chk = sharkMove[num - 1][d-1]
    if graph[x][y] == [0]:
        return
    myHome = []
    for i in chk:
        nx = x + dy[i]
        ny = y + dx[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        # 갈려는 곳에 페로몬이 있으면
        if len(pheromone[nx][ny]) != 0:
            # 본인것이면 저장
            if pheromone[nx][ny][0] == num:
                myHome.append([nx, ny, i])
                continue
            # 상어가 있으면
            elif pheromone[nx][ny][1] == K and pheromone[nx][ny][2] != 1:
                # 본인이 들어가있는 상어보다 숫자가 작으면 자리를 빼앗고 죽인다.
                if graph[nx][ny][0] > num:
                    graph[nx][ny] = [num, i]
                    pheromone[nx][ny] = [num, K, 1]
                    graph[x][y] = [0]
                # 본인이 더 작으면 그냥 소멸한다.
                else:
                    graph[x][y] = [0]
                break
            # 다른 페로몬향기가 맡아지면 도망간다.
            if pheromone[nx][ny][0] != num:
                continue

        # 빈칸에 이동하고 페로몬 저장
        if len(pheromone[nx][ny]) == 0:
            pheromone[nx][ny] = [num, K, 0]
            graph[nx][ny] = [num, i]
            graph[x][y] = [0]
        break
    #이동 못했으면 이전 페로몬 위치로 돌아간다.
    if graph[x][y][0] == num and len(pheromone[x][y]) != 0 and pheromone[x][y][0] == num:
        graph[myHome[0][0]][myHome[0][1]] = [num, myHome[0][2]]
        pheromone[myHome[0][0]][myHome[0][1]] = [num, K, 1]
        graph[x][y] = [0]

def remove():
    global pheromone, N
    for i in range(N):
        for j in range(N):
            if len(pheromone[i][j]) != 0:
                pheromone[i][j][1] -= 1
                if pheromone[i][j][2] == 1:
                    pheromone[i][j][2] = 0
                if pheromone[i][j][1] == 0:
                    pheromone[i][j] = []

remove()
cnt = 0
while True:
    shark = []
    for k in range(1,M+1):
        for i in range(N):
            for j in range(N):
                if graph[i][j][0] == k:
                    shark.append([graph[i][j][0], i, j, graph[i][j][1]])
    if len(shark) == 1:
        print(cnt)
        break
    for num, x, y, d in shark:
        move(num, x, y, d)
    remove()
    if cnt == 1000:
        print(-1)
        break
    cnt += 1



