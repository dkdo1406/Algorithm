"""
C만큼 바둑이를 태울 수 있으며 N마리가 주어진다.
바둑이를 태울 수 있는 최대 수를 출력하라

tsum을 이용해 해결
전체 합 - 현재원소 = 남은원소를 뜻함
sum(필터링한 원소) + (전체 합 - 현재원소)가 최대값보다 작으면 계산 안하게 함으로써 타임아웃 안걸리게 된다.
"""

C,N = map(int,input().split())
lst= [int(input()) for i in range(N)]
answer = 0
total = sum(lst)


def DFS(L,sum,tsum):
    global answer
    if sum+(total-tsum)<answer or sum>C or answer==C:
        return

    if L==len(lst):
        answer = max(answer,sum)
    else:
        DFS(L+1,sum+lst[L],tsum+lst[L])
        DFS(L + 1, sum,tsum+lst[L])

DFS(0,0,0)
print(answer)
