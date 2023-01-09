import sys
input = lambda: sys.stdin.readline()
result = []
while True:
    try:
        a,b = map(int,input().split())
        result.append(a+b)
    except:
        break
for i in range(len(result)-1):
    print(result[i])

