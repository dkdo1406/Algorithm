#4 2 1  N : 크기 ,M : 파이어볼 갯수, K : 이동 횟수
# 1 1 5 2 2 파이어볼 정보 , 행, 열, 질량, 속력, 방향 ri, ci, mi, si, d
# 1 4 7 1 6

N, M, K = list(map(int,input().split()))

graph = [[[] for _ in range(N)] for _ in range(N)]
countGraph = [[0]*N for _ in range(N)]
fireballs = []
for i in range(M):
    r,c,m,s,d = list(map(int,input().split()))
    fireballs.append([r-1,c-1,m,s,d])

# 파이어볼 정보 , 행, 열, 질량, 속력, 방향 ri, ci, mi, si, d
def move(r,c,m,s,d):
    global graph, countGraph
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    nx = ((dx[d] * s + N * 1000) + c) % N
    ny = ((dy[d] * s + N * 1000) + r) % N
    graph[ny][nx].append([r,c,m,s,d])
    countGraph[ny][nx] += 1
    print(r,c,m,s,d)
    for i in graph:
        print(i)
    print()
def mix(r,c,cnt):
    global countGraph, graph, fireballs
    countGraph[r][c] -= cnt
    totalM = 0
    totalS = 0
    isOdd = True
    isEven = True
    for _,_,m,s,d in graph[r][c]:
        totalM += m
        totalS += s
        if d % 2 == 0:
            isOdd = False
        if d % 2 != 0:
            isEven = False
    graph[r][c] = []
    if totalM // 5 > 0:
        m = totalM // 5
        s = totalS // cnt
        if isEven and isOdd:
            fireballs.append([r ,c, m, s, 1])
            fireballs.append([r, c, m, s, 3])
            fireballs.append([r, c, m, s, 5])
            fireballs.append([r, c, m, s, 7])
        else:
            fireballs.append((r, c, m, s, 0))
            fireballs.append((r, c, m, s, 2))
            fireballs.append((r, c, m, s, 4))
            fireballs.append((r, c, m, s, 6))


cnt = 0

for _ in range(K):
    cnt +=1
    print(fireballs)
    for r, c, m, s, d in fireballs:
        move(r, c, m, s, d)
    for i in graph:
        print(i)
    print()
    for i in countGraph:
        print(i)
    print()
    fireballs = []
    mixfireball = []
    for i in range(len(countGraph)):
        for j in countGraph[i]:
            if countGraph[i][j] > 1:
                mixfireball.append((i,j,countGraph[i][j]))
            elif countGraph[i][j] == 1:
                for k in graph[i][j]:
                    fireballs.append(k)
                    graph[i][j] = []


    for r,c,cnt in mixfireball:
        mix(r,c,cnt)


# for i in
# 결과 코드




