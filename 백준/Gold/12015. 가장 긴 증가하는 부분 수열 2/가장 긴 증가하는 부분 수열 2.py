import sys
import bisect
input = lambda : sys.stdin.readline()

n = int(input())

arr = list(map(int, input().split()))
LIS = [0]
LIS[0] = arr[0]

answer = 1
for i in range(1, n):
    if LIS[-1] < arr[i]:
        LIS.append(arr[i])
    elif LIS[0] > arr[i]:
        LIS[0] = arr[i]
    else:
        idx = bisect.bisect_left(LIS, arr[i])
        if arr[i] != LIS[idx]:
            LIS[idx] = arr[i]
    answer = max(answer, len(LIS))
print(answer)