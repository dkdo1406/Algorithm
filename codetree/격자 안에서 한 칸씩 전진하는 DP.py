n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
new_graph = [[0 for _ in range(n)] for _ in range(n)]
new_graph[0][0] = graph[0][0]
for i in range(1,n):
    new_graph[i][0] = graph[i][0] + new_graph[i-1][0]
    new_graph[0][i] = graph[0][i] + new_graph[0][i-1]
for i in range(1,n):
    for j in range(1,n):
        new_graph[i][j] = max(new_graph[i-1][j] + graph[i][j], new_graph[i][j-1] + graph[i][j])

