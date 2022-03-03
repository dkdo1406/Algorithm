import sys
input = lambda : sys.stdin.readline()
# A*(B+C)
# ABC+*
# 우선순위 : 괄호,
a = input()
a= a.replace('\n','')
temp = []
result = []
go = ['+','-']
stop = ['(',')','*','/']
for i in a:
    temp.append(i)
    # if i in go:
print(temp)


