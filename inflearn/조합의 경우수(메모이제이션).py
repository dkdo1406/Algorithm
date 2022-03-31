"""
5C3 = 10
5*4*3/3*2*1

#1 강의 보고 해결
nCr = n-1Cr-1 + n-1Cr 을 이용해 문제 풀이할 것
r=0 이거나  n==r 이면 종료
메모이제이션이란 이전에 계산한 값을 저장해 반복수행 제거하는것임 (DP문제의 핵심)

#2 메모이제이션 모르는 상태에서 해결, O(N)
"""
M,N = map(int,input().split())
answer = 0
memory = [[0]*(N+1) for i in range(M+1)]

#메모이제이션 사용안하고 함
def DFS_nomem(n,r):
    global answer
    if n==r or r==0:
        answer +=1
        return
    else:
        DFS_nomem(n-1,r-1)
        DFS_nomem(n-1,r)
#메모이제이션 사용
def DFS_mem(n,r):
    if memory[n][r]!=0:
        return memory[n][r]
    if n==r or r==0:
        memory[n][r]=1
        return memory[n][r]
    else:
        memory[n][r] = DFS_mem(n-1,r-1)+DFS_mem(n-1,r)
        return memory[n][r]
print(DFS_mem(M,N))
"""
#2
for i in range(N):
    answer *= (M-i)
for i in range(N):
    answer //= (N-i)
print(answer)
"""