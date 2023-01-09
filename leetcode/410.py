"""
num에 있는 것들을 m개로 나눠잔 집합의 합이 가장 큰 값을 출력
nCr인가?
5개를 2개만 뽑을 확률
"""
nums = [7,2,5,10,8]
m = 3
visited = [False]*len(nums)
temp =[]
answer = 0
def DFS(L):
    if L==m-1:
        test = 0
        for i,j in enumerate(visited):
            if j:
                test += sum(nums[:i])
                print(i,end=' ')
        print(temp)
        print(test)
        return
    else:
        for i in range(1,len(nums)):
            if not visited[i]:
                visited[i]=True
                temp.append(i)
                DFS(L+1)
                visited[i]=False
                temp.pop()

print(DFS(0))