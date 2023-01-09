N,M = list(map(int,input().split()))
graph = []
move = []
for i in range(N):
    graph.append(list(map(int,input().split())))

for i in range(M):
    move.append(list(map(int,input().split())))

cloud = [(N-1,0), (N-1, 1), (N-2, 0), (N-2, 1)]

def moveCloud(direction, count):
    tempCloud = []
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]
    for i in range(count):
    # if direction == 1:




for i in move:
    moveCloud(i[0],i[1])
    addWater()
    wartBug()
