N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
player = [i for i in range(N)]
totalTeam = set(player)
def combi(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combi(arr[i+1:], r-1):
                yield  [arr[i]] + next
def permu(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in permu(arr, r-1):
                yield [arr[i]] + next
answer = 10000000001
for i in combi(player,N//2):
        teamA = tuple(i)
        teamB = tuple(totalTeam - set(i))
        resultA = 0
        resultB = 0
        for j,k in permu(teamA,2):
            resultA += graph[j][k]
        for j, k in permu(teamB,2):
            resultB += graph[j][k]
        answer = min(abs(resultA - resultB), answer)
print(answer)