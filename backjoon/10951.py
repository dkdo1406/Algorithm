import sys
input = lambda: sys.stdin.readline()
result = []
while True:
    try:
        a,b = map(int,input().split())
        print(a+b)
    except:
        break

