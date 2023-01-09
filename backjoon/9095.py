n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

for m in arr:
    arr = [0] * 4
    if m < 4:
        arr[0] = 0
        arr[1] = 1
        arr[2] = 2
        arr[3] = 4
        print(arr[m])
        continue
    arr = [0] * (m+1)
    arr[0] = 0
    arr[1] = 1
    arr[2] = 2
    arr[3] = 4
    for i in range(4, m+1):
        arr[i] = arr[i-1] + arr[i-2] + arr[i-3]
    print(arr[m])