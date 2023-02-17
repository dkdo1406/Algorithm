arr = [int(input()) for _ in range(9)]

M = sum(arr)
S = set(arr)
arr.sort()
for l in range(8):
    M -= arr[l]
    r = l
    r += 1
    while r < 9:
        M -= arr[r]
        if M == 100:
            S.remove(arr[l])
            S.remove(arr[r])
            break
        M += arr[r]
        r += 1
    if len(S) == 7:
        break
    M += arr[l]


for i in sorted(list(S)):
    print(i)