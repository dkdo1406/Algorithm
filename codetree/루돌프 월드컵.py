arr = list(map(int, input().split()))

# 1번 루돌프가 2등안에 들 확률
# 이길경우 3점 비길경우 1점 졌을경우 0점

fight = [[0,1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]
graph1 = [[0 for _ in range(4)] for _ in range(4)]
result = 0
def calc_score(graph):
    answer = 1
    for i in range(0,4):
        for j in range(i+1,4):
            if graph[i][j] == 3:
                answer *= (4 * arr[i]) / ((5 * arr[i]) + (5 * arr[j]))
            elif graph[i][j] == 0:
                answer *= (4 * arr[j]) / ((5 * arr[i]) + (5 * arr[j]))
            elif graph[i][j] == 1:
                answer *= (arr[i]+arr[j]) / ((5 * arr[i]) + (5 * arr[j]))

    return answer
def BFS(L, graph):
    global result
    if L == 6:
        score = []
        for i in graph:
            score.append(sum(i))
        cnt = 0
        for i in range(1,4):
            if score[0] >= score[i]:
                cnt += 1
        if cnt > 1:
            result = result + calc_score(graph)
        return
    i,j = fight[L]

    graph[i][j] = 3
    graph[j][i] = 0
    BFS(L+1, graph)

    graph[i][j] = 0
    graph[j][i] = 3
    BFS(L+1, graph)

    graph[i][j] = 1
    graph[j][i] = 1
    BFS(L+1, graph)

BFS(0, graph1)

print(f"{result*100:.3f}")

