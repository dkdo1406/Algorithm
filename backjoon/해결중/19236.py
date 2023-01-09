N, M, K = list(map(int, input().split()))
# graph = [list(map(int, input().split())) for i in range(N)]
# graph에 담을 것 : 번호, K
graph = [[[] for _ in range(N)] for _ in range(N)]
dx = [0, 0, 0, -1 ,1]
dy = [0, -1, 1, 0, 0]
for i in graph:
    print(i)
for num in list(map(int, input().split())):
    for i in range(N):
        for j in range(N):
            if num != 0:
                graph[i][j].append([num,K])
            else:
                graph[i][j].append(0)
for i in graph:
    print(i)
sharkMove = [[list(map(int, input().split())) for i in range(4)] for i in range(M)]

for i in graph:
    print(i)

