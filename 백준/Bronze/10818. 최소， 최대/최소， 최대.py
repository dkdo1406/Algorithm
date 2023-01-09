import sys
input = lambda : sys.stdin.readline()

n = int(input())
lst = list(map(int,input().split(' ')))
print(min(lst),max(lst))