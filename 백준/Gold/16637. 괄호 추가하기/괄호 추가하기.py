n = int(input())
arr = []
for i in input():
    if i.isdigit():
        arr.append(int(i))
    else:
        arr.append(i)

def calc(arr):
    result = 0
    operator = ''
    for index, i in enumerate(arr):
        if index == 0:
            result = i
        elif index % 2 != 0:
            operator = i
        else:
            if operator == '+':
                result += i
            elif operator == '-':
                result -= i
            elif operator == '*':
                result *= i
    return result

answer = -2 ** 31

def DFS(L, new_arr):
    global answer
    if L >= n:
        answer = max(answer, calc(new_arr))
        return
    DFS(L + 1, new_arr + [arr[L]])
    if L % 2 == 0:
        DFS(L+3, new_arr + [calc(arr[L:L+3])])

if n == 1:
    print(arr[0])
else:
    DFS(0, [])
    print(answer)
