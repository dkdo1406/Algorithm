from collections import deque
import sys
input = lambda : sys.stdin.readline()
h, k, r = list(map(int, input().split()))
q = deque()
arr = [0] * ((2 ** (h+1))-1)
for i in range(2 ** h):
    temp = list(map(int, input().split()))
    arr[i] = deque(temp)
for i in range(2**h, len(arr)):
    arr[i] = [deque(), deque()]
day = 1

answer = [0]
def check():
    global answer
    cnt = len(arr)
    for i in range(len(arr)-1, (2**h)-1, -1):
        if i == len(arr)-1:
            if day % 2 == 0:
                if arr[i][1]:
                    answer.append(arr[i][1].popleft())
            else:
                if arr[i][0]:
                    answer.append(arr[i][0].popleft())
        else:
            if day % 2 == 0:
                if arr[i][1]:
                    if i % 2 == 0:
                        arr[cnt][0].append(arr[i][1].popleft())
                    else:
                        arr[cnt][1].append(arr[i][1].popleft())
            else:
                if arr[i][0]:
                    if i % 2 == 0:
                        arr[cnt][0].append(arr[i][0].popleft())
                    else:
                        arr[cnt][1].append(arr[i][0].popleft())
        if i % 2 == 0:
            cnt -= 1
for _ in range(r):
    check()
    if k != 0:
        temp = (2 ** h) - 1
        for i in range(2**h):
            if i % 2 == 0:
                temp += 1
                arr[temp][0].append(arr[i].popleft())
            else:
                arr[temp][1].append(arr[i].popleft())
        k -= 1
    day += 1

print(sum(answer))