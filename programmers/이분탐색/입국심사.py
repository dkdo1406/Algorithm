"""
https://programmers.co.kr/learn/courses/30/lessons/43238?language=python3
n명의 입국자가 있다.
times에 시간만큼 입국심사하는데 시간이 걸린다.
가장 짧은 입국심사 시간은?
7 10 14 20 21 28 30
20일때 20을 안하고 21을 함으로써 28분에 끝남
N    times  return
6	[7, 10]	28
"""
import collections
n=6
times = [10,7]
times.sort()
left,right = 0,n*times
print(left,right)

exit()
times.sort()
q = collections.deque()
for i in times:
    q.append(i)
q1 = collections.deque()
cnt=0
while cnt!=n:
    V =q.popleft()
    q1.append(V*2)
    q.append(V*2)
    cnt+=1
print(q)
