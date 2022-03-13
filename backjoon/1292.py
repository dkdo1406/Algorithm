"""
1,2,2,3,3,3,4,4,4,4...
이렇게 되어있는 수열에서 주어진 구간의 합을 출력하라
ex 3 7
2 3 3 3 4을 더하면 15

"""
lt,rt =map(int,input().split())
lst=[]
for i in range(rt+1):
    lst.extend([i]*i)
if lt==rt:
    print(lst[lt-1])
else:
    print(sum(lst[lt-1:rt]))
