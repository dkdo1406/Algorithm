"""
송아지는 수직선상 좌표점에 위치
현수는 앞으로 1칸 뒤로 1칸 앞으로 5칸 총 3가지방법 사용가능
송아지까지 최단 점프 횟수?
좌표는 1~10000
5 14
3
"""
import collections
hyn,cow = 5,14
# 1,-1,5를 순서대로 대입 후 BFS로 한다?
def BFS(me,loc):
    jump = [1,-1,5]
    q = collections.deque()
    q.append(me)
    L=0
    visited = [False]*100001
    if me ==loc:
        print(L)
        exit()
    while q:
        for _ in range(len(q)):
            tmp = q.popleft()
            for i in jump:
                if not visited[tmp+i]:
                    q.append(tmp+i)
                    visited[tmp+i] = True
        L+=1
        if loc in q:
            print(L)
            exit()

BFS(hyn,cow)
