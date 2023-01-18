A = int(input())
B = int(input())
C = int(input())
result = A*B*C
answer = [0] * 10
for i in list(str(result)):
    answer[int(i)] += 1
for i in answer:
    print(i)