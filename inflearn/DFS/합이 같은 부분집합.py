"""
예를 들어 {1, 3, 5, 6, 7, 10}이 입력되면 {1, 3, 5, 7} = {6, 10} 으로 두 부분집합의 합이 16으로 같은 경우가 존재하는 것을 알 수 있다.
같으면 "YES" 다르면 "NO" 출력

"""
N = int(input())
lst = list(map(int,input().split()))
visted = [0]*(N+1)
total = sum(lst)
answer = "NO"
def BFS(L,sum):
    global answer
    if sum>total/2 or answer =="YES":
        return
    if L==N:
        if (total-sum)==sum:
            answer = "YES"
            return answer
    else:
        BFS(L+1,sum+lst[L]) #lst[L]가 있을 떄
        BFS(L+1,sum) #lst[L]가 없을 때

BFS(0,0)
print(answer)