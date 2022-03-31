"""
5
1 5 7 11 15
40
나는 나누기로 했는데 강의는 더하기를 추천함

내가 만든 코드 : lst[L]마다 for문을 돌림
고친코드 : 내림차순으로 바꾼 후 더함
"""

N = int(input())
lst = list(map(int,input().split()))
money = int(input())
lst = list(reversed(lst))

answer = money//lst[-1] #만들수있는 최대 수

def DFS(L,sum):
    global answer,lst
    if sum>money or L>answer:
        return
    if sum==money:
        answer = min(answer,L)
        return
    else:
        for i in lst:
            DFS(L+1,sum+i)
DFS(0,0)
print(answer)

"""
def DFS(L,M,cnt,lst):
    global answer
    if M==0:
        answer = min(answer,cnt)
        return
    if L==N or answer<cnt: # 동전을 모두 사용했거나 남은 돈이 0일 때 종료
        return
    else:
        DFS(L + 1, M, cnt, lst)  # 사용X

        for i in range((M//lst[L]),0,-1):
            DFS(L + 1, M - (lst[L] * i), cnt + i, lst)  # 1개이상 사용할 경우

DFS(0,money,0,lst)
"""