import sys
input = lambda : sys.stdin.readline()
N = int(input())
M = []
for i in range(N):
    M.append(list(map(int,input().split())))
M.sort(key= lambda x: (x[0],x[1]))
for i in M:
    print(i[0],i[1])
