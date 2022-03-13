"""
입력 3

출력
1 2 3
1 2
1 3
1
2 3
2
3
"""
global n
global ch
n=3
ch = [0]*(n+1)

def DFS(L):
    global n
    global ch
    if L == n+1:
        for i,j in enumerate(ch):
            if j==1:
                print(i,end=' ')
        print()
    else:
        ch[L]=1
        DFS(L + 1)

        ch[L] = 0
        DFS(L + 1)

DFS(1)