n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
new_graph = [[0 for _ in range(n)] for _ in range(n)]
new_graph[0][0] = [graph[0][0], graph[0][0]]
new_graph[n-1][n-1] = [graph[n-1][n-1], graph[n-1][n-1]]

for i in range(1, n):
    new_graph[i][0] = [min(graph[i][0], new_graph[i-1][0][0]), max(graph[i][0], new_graph[i-1][0][1])]
    new_graph[0][i] = [min(graph[0][i], new_graph[0][i-1][0]), max(graph[0][i], new_graph[0][i-1][1])]
for i in range(1, n-1):
    new_graph[n-1][n-i-1] = [min(graph[n-1][n-i-1], new_graph[n-1][n-i][0]), max(graph[n-1][n-i-1], new_graph[n-1][n-i][1])]
    new_graph[n-i-1][n-1] = [min(graph[n-i-1][n-1], new_graph[n-i][n-1][0]), max(graph[n-i-1][n-1], new_graph[n-i][n-1][1])]
for i in new_graph:
    print(i)

# for i in range()

# for i in range(n-1, 0, -1):
#     for j in range(n-1, 0, -1):
#         if i == n-1 and j == n-1 :
#             continue
#         new_graph[i][j] =
for i in range(1, n):
    for j in range(1, n):
        p1_min = min(graph[i][j], new_graph[i - 1][j][0])
        p1_max = max(graph[i][j], new_graph[i - 1][j][1])
        p2_min = min(graph[i][j], new_graph[i][j - 1][0])
        p2_max = max(graph[i][j], new_graph[i][j - 1][1])

        if abs(p1_max - p1_min) < abs(p2_max - p2_min):
            new_graph[i][j] = [p1_min, p1_max]
        elif abs(p1_max - p1_min) > abs(p2_max - p2_min):
            new_graph[i][j] = [p2_min, p2_max]
        else:
            new_graph[i][j] = [min(p1_min, p2_min), min(p1_max, p2_max)]

print(abs(new_graph[n-1][n-1][1]-new_graph[n-1][n-1][0]))