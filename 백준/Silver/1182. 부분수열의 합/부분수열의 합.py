N, S = list(map(int, input().split()))
arr = list(map(int, input().split()))
answer = 0
answer_visited = dict()
def DFS(L, result):
    global answer
    if L == N:
        return
    result += arr[L]
    if result == S:
        answer += 1

    DFS(L+1, result)
    DFS(L+1, result - arr[L])
DFS(0,0)
print(answer)