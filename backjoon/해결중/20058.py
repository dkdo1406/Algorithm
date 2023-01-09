import copy

N, Q = list(map(int, input().split()))
S = 2 ** N
graph = [list(map(int,input().split())) for _ in range(S)]
L = list(map(int, input().split()))

def rotate():
    pass
# newGraph = copy.deepcopy(graph)
# test = [2,0]
# for R in range(2, 4):
#     for C in range(0, 2):
#         a = test[0] + 2 - C - 1
#         newGraph[R][C] = graph[a][R]
# for i in newGraph:
#     print(i)
# exit()
def slide(num):
    global graph
    num = 2 ** num

    nowR, nowC,cnt = 0, 0, 1
    gogo = len(graph) // num
    print(gogo)
    newGraph = copy.deepcopy(graph)
    for newR in range(gogo):
        for newC in range(gogo):
            for R in range(nowR, nowR + num):
                for C in range(nowC, nowC + num):
                    print(nowR, nowC)
                    a = nowR + num * cnt - C - 1
                    print(a)
                    # newGraph[R][C] = graph[a][R]

                    y = R + num * newR
                    x = C + num * newC
                    print(y,x,R,C)
                    newGraph[R][C] = graph[y][x]
                    # b = R
                    # print(R,C,a,b)
                    # print(nowY)
                    # print(nowX, nowY)
            cnt += 1
            nowR += num
            if nowR == len(graph):
                nowR = 0
                cnt = 1

        nowC += num
    for i in newGraph:
        print(i)
    print()
    for i in graph:
        print(i)
for i in graph:
    print(i)
print()
for i in L:
    slide(i)