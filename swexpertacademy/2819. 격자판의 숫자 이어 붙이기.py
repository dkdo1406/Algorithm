from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(4)]

dx = [0,0, -1, 1]
dy = [1,-1,0,0]

# 격자의 위치는 임의의 위치이다.
# 동서남북으로 총 6번 이동한다.
# 이동할 떄 지나갔던 곳을 다시 갈 수 있으며 0으로 시작하는 숫자 생성 가능
# lst = [[[i,j] for j in range(4)] for i in range(4)]
lst = []
for i in range(4):
    for j in range(4):
        lst.append((i,j))
def combi(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combi(arr[i+1:], r-1):
                yield [arr[i]] + next

def bfs(x,y):
    global dx,dy, graph
    q = deque()
    L = 1
    q.append([L,x,y,str(graph[x][y])])

    while q:
        L, newX, newY, temp = q.popleft()
        if L == 7:
            # 여기서 구분을 하는게 좋을듯
            total = []
            total.append(temp)
            for _,_,_,i in q:
                total.append(i)
            return total
        for i in range(4):
            nx = newX + dy[i]
            ny = newY + dx[i]
            if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
                continue
            q.append([L+1,nx,ny, temp + str(graph[nx][ny])])

a = combi([1,2,3,4],3)
result = 0
total = []
for i in lst:
    print(i)
    temp = bfs(i[0],i[1])
    total+= temp

total = set(total)
print(len(total))