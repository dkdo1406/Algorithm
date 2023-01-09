n = int(input())
dic = dict()

def check(arr):
    if arr[0] == "add":
        k = int(arr[1])
        v = int(arr[2])
        dic[k] = v
    elif arr[0] == "find":
        k = int(arr[1])
        if k in dic:
            print(dic[k])
        else:
            print(None)

    elif arr[0] == "remove":
        k = int(arr[1])
        dic.pop(k)

for i in range(n):
    arr = list(input().split())
    check(arr)


