N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = 0
def DFS(L, result):
    global answer
    if L >= N:
        answer = max(answer, result)
        return
    if L + arr[L][0] <= N:
        DFS(L+arr[L][0], result + arr[L][1])
    DFS(L+1, result)

DFS(0, 0)
print(answer)