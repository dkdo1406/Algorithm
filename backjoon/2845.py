A,B = map(int,input().split())
lst = map(int,input().split())
answer = []
people = A*B
for i in lst:
    print(i-people,end=' ')
    answer.append(i-people)
# print(answer)