import sys
input = lambda : sys.stdin.readline()
N, K = list(map(int, input().split()))
arr = list(input())
robots = []
new_arr = [0] * N
for i in range(len(arr)):
    if arr[i] == "P":
        robots.append(i)
        new_arr[i] = 1
answer = 0
def DFS(L, result):
    global answer
    if sum(result) - L <= answer:
        return
    if L == len(robots):
        answer = max(answer, sum(result)-len(robots))
        return
    for i in range(1,K+1):
        if robots[L]+i < N and result[robots[L] + i] == 0:
            result[robots[L] + i] = 1
            DFS(L+1, result)
            result[robots[L] + i] = 0
        if robots[L] - i >= 0 and result[robots[L] - i] == 0:
            result[robots[L] - i] = 1
            DFS(L + 1, result)
            result[robots[L] - i] = 0
    DFS(L + 1, result)
DFS(0, new_arr)
print(answer)