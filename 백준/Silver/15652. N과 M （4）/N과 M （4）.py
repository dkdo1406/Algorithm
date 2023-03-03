N, M = list(map(int, input().split()))

def permu(arr ,cnt, i):
    if cnt == M:
        for i in arr:
            print(i, end=" ")
        print()
        return
    else:
        for j in range(i, N + 1):
            permu(arr + [j], cnt + 1, j)
permu([], 0, 1)

