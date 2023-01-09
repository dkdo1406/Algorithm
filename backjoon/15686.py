N,M = list(map(int, input().split()))

graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

chicken = []
home = []
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == 2:
            chicken.append((i,j))
        if graph[i][j] == 1:
            home.append((i,j))

def combi(arr, n):
    result = []
    if n ==0:
        return [[]]

    for i in range(0, len(arr)):
        elem = arr[i]
        rest_arr = arr[i + 1:]
        for C in combi(rest_arr, n-1):
            result.append([elem]+C)

    return result

result = 100000000001
for i in combi(chicken, M):
    answer = 0
    for h_x,h_y in home:
        minResult = 101
        for x,y in i:
            minResult = min(abs(h_x - x) + abs(h_y - y), minResult)
        answer += minResult
    result = min(answer, result)

print(result)