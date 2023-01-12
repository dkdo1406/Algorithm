n = int(input())
arr = [0] * (n+1)
answer = n+1

def DFS(L, result):
    global answer
    if answer < result[L]:
        return
    if L == 1:
        answer = min(answer, result[L])
        return
    if L % 3 == 0:
        if result[L // 3] == 0 or result[L // 3] > result[L] + 1:
            result[L // 3] = result[L] + 1
            DFS(L // 3, result)
    if L % 2 == 0:
        if result[L // 2] == 0 or result[L // 2] > result[L] + 1:
            result[L // 2] = result[L] + 1
            DFS(L // 2, result)
    if result[L - 1] == 0 or result[L - 1] > result[L] + 1:
        result[L-1] = result[L] + 1
        DFS(L - 1, result)

DFS(n, arr)
print(answer)