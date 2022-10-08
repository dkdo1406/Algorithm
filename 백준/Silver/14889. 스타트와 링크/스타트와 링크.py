from  itertools import combinations
from itertools import  permutations
N = int(input())

graph = [list(map(int,input().split())) for _ in range(N)]
playerIdx = [i for i in range(N)]
totalTeam = set(playerIdx)

answer = 10000000
for i in combinations(playerIdx,N//2):
    AtemaPoint = 0
    BteamPoint = 0
    Ateam = i
    Bteam = tuple(totalTeam - set(Ateam))

    for i2, j2 in permutations(Ateam,2):
        AtemaPoint += graph[i2][j2]
    for i3, j3 in permutations(Bteam, 2):
        BteamPoint += graph[i3][j3]
    answer = min(abs(AtemaPoint - BteamPoint), answer)
print(answer)