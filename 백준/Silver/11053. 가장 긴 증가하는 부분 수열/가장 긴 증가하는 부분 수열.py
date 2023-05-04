import bisect
N = int(input())
arr = list(map(int, input().split()))

ans = []
for i in arr:
    if not ans or i > ans[-1]:
        ans.append(i)
    else:
        index = bisect.bisect_left(ans, i)
        ans[index] = i

print(len(ans))