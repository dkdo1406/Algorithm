from collections import deque
graph = []
for i in range(7):
  graph.append(list(map(int, input().split())))

dr = [0,0,1,-1]
dc = [1,-1,0,0]
def bfs():
  q = deque()
  q.append([0,0])
  graph[0][0]=1
  while q:
    r,c = q.popleft()
    for i in range(4):
      nr = dr[i] + r
      nc = dc[i] + c
      if nr < 0 or nr >= 7 or nc < 0 or nc >= 7 or graph[nr][nc] > 0:
        continue
      graph[nr][nc] = graph[r][c] + 1
      q.append([nr,nc])
bfs()

if graph[6][6] == 0:
  print(-1)
else:
  print(graph[6][6] - 1)
