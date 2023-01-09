n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
new_graph = [[1 for _ in range(n)] for _ in range(n)]
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
cell = []

for r in range(n):
    for c in range(n):
        cell.append([graph[r][c], r, c])
cell.sort()

for _, r, c in cell:
    for i in range(4):
        nr = dr[i] + r
        nc = dc[i] + c
        if nr < 0 or nr >= n or nc < 0 or nc >= n or graph[nr][nc] <= graph[r][c]:
            continue
        new_graph[nr][nc] = max(new_graph[nr][nc], new_graph[r][c] + 1)
answer = 0
for r in range(n):
    for c in range(n):
        answer = max(answer, new_graph[r][c])
print(answer)