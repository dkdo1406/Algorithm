"""
N, M , target 이 있을 때
N/M의 target번째 소수점을 구하라.
target이 1,000,000이 넘어 직접 연산해줘야 한다.
"""
n,m,target = map(int,input().split())

answer = 0
cnt =0
while cnt<target:
    if n<10:
        n = (n*10)%m
        answer = (n+10)//m
        cnt += 1
    else:
        n = n%m

print(answer)
print(25/7)