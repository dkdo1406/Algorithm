n = int(input())
arr = [int(input()) for _ in range(n)]
arr[0] = [arr[0], 0]
if n > 1:
    arr[1] = [arr[0][0]+arr[1], arr[1]]
    for i in range(2, n):
        arr[i] = [arr[i-1][1] + arr[i], max(arr[i-2]) + arr[i]]
print(max(arr[n-1]))