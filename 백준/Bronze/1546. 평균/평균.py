n = int(input())
arr = list(map(int, input().split()))
answer = 0

value = max(arr)
new_arr = []
for i in arr:
    new_arr.append(i/value*100)
print(sum(new_arr)/n)