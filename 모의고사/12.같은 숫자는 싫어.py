arr = [4, 4, 4, 3, 3]
# result = [1,3,0,1]
result = []
result.append(arr[0])
for i in range(1, len(arr)):
    if arr[i - 1] != arr[i]:
        result.append(arr[i])
print(result)
