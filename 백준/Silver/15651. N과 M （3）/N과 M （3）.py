N, M = list(map(int, input().split()))

"""
1부터 N까지 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.

"""

def permu(arr ,cnt):
    if cnt == M:
        for i in arr:
            print(i, end=" ")
        print()
        return
    else:
        for i in range(1, N + 1):
            permu(arr + [i], cnt + 1)
permu([], 0)

