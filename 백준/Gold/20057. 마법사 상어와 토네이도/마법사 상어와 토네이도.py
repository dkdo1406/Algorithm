import math

N = int(input())

graph = []
for i in range(N):
    graph.append(list(map(int,input().split())))

start= [N//2,N//2]

graphs = [[0]*N for i in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0 #회전인데 회전하는경우는 칸만큼 가면 회전한다.
count = 1 # 몇칸 갈지 저장, recount가 2번 0이되면 +1이 증가한다.
reCount = 1 # 그만큼 칸가면 +1된 count 저장
tmpCount = 1

nx = N//2
ny = N//2
result = 0
def windy(sand):
    alpha = sand - (math.floor(sand * 0.01) + math.floor(sand * 0.01) +
                    math.floor(sand * 0.07) + math.floor(sand * 0.07) +
                    math.floor(sand * 0.1) + math.floor(sand * 0.1) +
                    math.floor(sand * 0.02)+ math.floor(sand * 0.02) + math.floor(sand * 0.05))
    return alpha

def tornado(x,y,sand,cnt):
    global graph, result, N
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    graph[x][y] = 0
    if cnt == 0:
        # 5,10,10,7,7,2,2,1,1
        nx = [-2, -1, -1, 0, 0, 0, 0, 1, 1]
        ny = [0, -1, 1, -1, 1, -2, 2, -1, 1]
        # 일단 흩날려보자
        bx = x + dy[cnt]
        by = y + dx[cnt]
        if bx >= 0 and bx < N and by >= 0 and by < N:
            graph[x + dy[cnt]][y + dx[cnt]] += windy(sand)
        else:
            result += windy(sand)

        for i in range(9):
            bx = x + ny[i]
            by = y + nx[i]
            if i == 0:
                if bx >= 0 and bx < N and by >= 0 and by < N:
                    graph[bx][by] += math.floor(sand * 0.05)
                else:
                    result += math.floor(sand * 0.05)
            if i == 1 or i == 2:
                if bx >= 0 and bx < N and by >= 0 and by < N:
                    graph[bx][by] += math.floor(sand * 0.1)
                else:
                    result += math.floor(sand * 0.1)
            if i == 3 or i == 4:
                if bx >= 0 and bx < N and by >= 0 and by < N:
                    graph[bx][by] += math.floor(sand * 0.07)
                else:
                    result += math.floor(sand * 0.07)

            if i == 5 or i == 6:
                if bx >= 0 and bx < N and by >= 0 and by < N:
                    graph[bx][by] += math.floor(sand * 0.02)
                else:
                    result += math.floor(sand * 0.02)

            if i == 7 or i == 8:
                if bx >= 0 and bx < N and by >= 0 and by < N:
                    graph[bx][by] += math.floor(sand * 0.01)
                else:
                    result += math.floor(sand * 0.01)

    if cnt == 1:
        # 5,10,10,7,7,2,2,1,1
        nx = [0, -1, 1, -1, 1, -2, 2, -1, 1]
        ny = [2, 1, 1, 0, 0, 0, 0, -1, -1]
        # 일단 흩날려보자
        bx = x + dy[cnt]
        by = y + dx[cnt]
        if bx >= 0 and bx < N and by >= 0 and by < N:
            graph[x + dy[cnt]][y + dx[cnt]] += windy(sand)
        else:
            result += windy(sand)

        for i in range(9):
            bx = x + ny[i]
            by = y + nx[i]
            if i == 0:
                if bx >= 0 and bx < N and by >= 0 and by < N:
                    graph[bx][by] += math.floor(sand * 0.05)
                else:
                    result += math.floor(sand * 0.05)
            if i == 1 or i == 2:
                if bx >= 0 and bx < N and by >= 0 and by < N:
                    graph[bx][by] += math.floor(sand * 0.1)
                else:
                    result += math.floor(sand * 0.1)
            if i == 3 or i == 4:
                if bx >= 0 and bx < N and by >= 0 and by < N:
                    graph[bx][by] += math.floor(sand * 0.07)
                else:
                    result += math.floor(sand * 0.07)

            if i == 5 or i == 6:
                if bx >= 0 and bx < N and by >= 0 and by < N:
                    graph[bx][by] += math.floor(sand * 0.02)
                else:
                    result += math.floor(sand * 0.02)

            if i == 7 or i == 8:
                if bx >= 0 and bx < N and by >= 0 and by < N:
                    graph[bx][by] += math.floor(sand * 0.01)
                else:
                    result += math.floor(sand * 0.01)

    if cnt == 2:
        # 5,10,10,7,7,2,2,1,1
        nx = [2, 1, 1, 0, 0, 0, 0, -1, -1]
        ny = [0, -1, 1, -1, 1, -2, 2, -1, 1]
        # 일단 흩날려보자
        bx = x + dy[cnt]
        by = y + dx[cnt]
        if bx >= 0 and bx < N and by >= 0 and by < N:
            graph[x + dy[cnt]][y + dx[cnt]] += windy(sand)
        else:
            result += windy(sand)

        for i in range(9):
            bx = x + ny[i]
            by = y + nx[i]
            if i == 0:
                if bx >= 0 and bx < N and by >= 0 and by < N:
                    graph[bx][by] += math.floor(sand * 0.05)
                else:
                    result += math.floor(sand * 0.05)
            if i == 1 or i == 2:
                if bx >= 0 and bx < N and by >= 0 and by < N:
                    graph[bx][by] += math.floor(sand * 0.1)
                else:
                    result += math.floor(sand * 0.1)
            if i == 3 or i == 4:
                if bx >= 0 and bx < N and by >= 0 and by < N:
                    graph[bx][by] += math.floor(sand * 0.07)
                else:
                    result += math.floor(sand * 0.07)

            if i == 5 or i == 6:
                if bx >= 0 and bx < N and by >= 0 and by < N:
                    graph[bx][by] += math.floor(sand * 0.02)
                else:
                    result += math.floor(sand * 0.02)

            if i == 7 or i == 8:
                if bx >= 0 and bx < N and by >= 0 and by < N:
                    graph[bx][by] += math.floor(sand * 0.01)
                else:
                    result += math.floor(sand * 0.01)

    if cnt == 3:
        # 5,10,10,7,7,2,2,1,1
        nx = [0, -1, 1, -1, 1, -2, 2, -1, 1]
        ny = [-2, -1, -1, 0, 0, 0, 0, 1, 1]
        # 일단 흩날려보자
        bx = x + dy[cnt]
        by = y + dx[cnt]
        if bx >= 0 and bx < N and by >= 0 and by < N:
            graph[x + dy[cnt]][y + dx[cnt]] += windy(sand)
        else:
            result += windy(sand)

        for i in range(9):
            bx = x + ny[i]
            by = y + nx[i]
            if i == 0:
                if bx >= 0 and bx < N and by >= 0 and by < N:
                    graph[bx][by] += math.floor(sand * 0.05)
                else:
                    result += math.floor(sand * 0.05)
            if i == 1 or i == 2:
                if bx >= 0 and bx < N and by >= 0 and by < N:
                    graph[bx][by] += math.floor(sand * 0.1)
                else:
                    result += math.floor(sand * 0.1)
            if i == 3 or i == 4:
                if bx >= 0 and bx < N and by >= 0 and by < N:
                    graph[bx][by] += math.floor(sand * 0.07)
                else:
                    result += math.floor(sand * 0.07)

            if i == 5 or i == 6:
                if bx >= 0 and bx < N and by >= 0 and by < N:
                    graph[bx][by] += math.floor(sand * 0.02)
                else:
                    result += math.floor(sand * 0.02)

            if i == 7 or i == 8:
                if bx >= 0 and bx < N and by >= 0 and by < N:
                    graph[bx][by] += math.floor(sand * 0.01)
                else:
                    result += math.floor(sand * 0.01)


while True:
    if nx == 0 and ny == 0:
        break
    tmp_nx = nx
    tmp_ny = ny
    nx = tmp_nx + dy[cnt%4]
    ny = tmp_ny + dx[cnt%4]

    # graph[nx][ny] = graph[tmp_nx][tmp_ny] + 1
    tornado(nx, ny, graph[nx][ny], cnt%4)
    reCount -=1

    if reCount == 0:
        cnt += 1
        reCount = count
        tmpCount += 1
        if tmpCount % 2 == 0:
            count += 1

print(result)
