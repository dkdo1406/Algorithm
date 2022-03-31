# n,m,target = map(int,input().split())
n=25
m=7
target=5
answer = 0
cnt =0
while cnt<target:
    if n<10:
        n = (n*10)%m
        answer = (n+10)//m
        cnt += 1
    else:
        n = n%m

print(n,cnt)
print(answer)
print(25/7)