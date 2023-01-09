def combi(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combi(arr[i:], r - 1):
                yield [arr[i]] + next

arr = [1, 2, 3, 4, 5]
for r in range(1, len(arr)+1):
	for combination in combi([1, 2, 3, 4, 5], r):
		print(combination)