import sys
input = lambda: sys.stdin.readline()
N, M = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()
def permutation(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in permutation(arr, r-1):
                yield [arr[i]] + next
for permu in permutation(arr, M):
    for i in permu:
        print(i,end='')
        print(" ",end='')
    print()