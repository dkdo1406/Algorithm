def combination(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combination(arr[i:], r-1):
                yield [arr[i]] + next
def permuta(prefix, k):
    if len(prefix) == r:
        yield prefix
    else:
        for i in range(k, len(arr)):
            arr[i], arr[k] = arr[k], arr[i]
            for next in permuta(prefix + [arr[k]], k+1):
                yield next
            arr[i], arr[k] = arr[k], arr[i]



def permutation(prefix, k):
    if len(prefix) == r:
        yield prefix
    else:
        for i in range(k, len(arr)):
            arr[i], arr[k] = arr[k], arr[i]
            for next in permutation(prefix + [arr[k]], k+1):
                yield next
            arr[i], arr[k] = arr[k], arr[i]

arr = [1,2,3,4,5]
r = 3
for combi in combination(arr,r):
    print(combi)
print()
for permu in permutation([], 0):
    print(permu)