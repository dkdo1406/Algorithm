import sys
from collections import deque
input = lambda : sys.stdin.readline()
n = int(input())
A = deque()
B = deque()
C = deque()
D = deque()
answer = [-1] * n
temp = 0
deadlock = False
def start(before, current):
    global deadlock
    if A and B and C and D:
        deadlock = True
        return
    while before < current and (A or B or C or D):
        waiting = [0,0,0,0]
        if A and not D:
            waiting[0] = 1
        if B and not A:
            waiting[1] = 1
        if C and not B:
            waiting[2] = 1
        if D and not C:
            waiting[3] = 1

        for i in range(4):
            if waiting[i] == 1:
                if i == 0:
                    answer[A.popleft()] = before
                elif i == 1:
                    answer[B.popleft()] = before
                elif i == 2:
                    answer[C.popleft()] = before
                elif i == 3:
                    answer[D.popleft()] = before
        before += 1

for i in range(n):
    t, road = list(input().split())
    t = int(t)
    if i == 0:
        temp = t
    if temp != t:
        start(temp, t)
        temp = t
    if deadlock:
        break
    else:
        if road == "A":
            A.append(i)
        elif road == "B":
            B.append(i)
        elif road == "C":
            C.append(i)
        elif road == "D":
            D.append(i)
    if A and B and C and D:
        deadlock = True

while not deadlock and (A or B or C or D):
    waiting = [0, 0, 0, 0]
    if A and not D:
        waiting[0] = 1
    if B and not A:
        waiting[1] = 1
    if C and not B:
        waiting[2] = 1
    if D and not C:
        waiting[3] = 1

    for i in range(4):
        if waiting[i] == 1:
            if i == 0:
                answer[A.popleft()] = temp
            elif i == 1:
                answer[B.popleft()] = temp
            elif i == 2:
                answer[C.popleft()] = temp
            elif i == 3:
                answer[D.popleft()] = temp
    temp += 1

for i in answer:
    print(i)
