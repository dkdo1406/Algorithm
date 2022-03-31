import collections
matrix = []
for r in range(7):
    matrix.append(list(map(int,input().split())))
move = {(0, 1), (0, -1), (1, 0), (0, -1)}
def BFS(x,y):
    q = collections.deque()

    q.append([x,y])
    while q:
        V = q.popleft()
        if V == [6,6]:
            return matrix[V[0]][V[1]]
        else:
            for i in move:
                if 0<=V[0]+i[0]<7 and 0<= V[1]+i[1]<7 and matrix[V[0]+i[0]][V[1]+i[1]]==0:
                    matrix[V[0]+i[0]][V[1]+i[1]] = matrix[V[0]][V[1]] +1
                    q.append([V[0]+i[0],V[1]+i[1]])
    return -1
print(BFS(0,0))
for i in matrix:
    print(i)
