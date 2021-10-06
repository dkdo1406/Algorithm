"""
1-1. 입력된 수가 짝수라면 2로 나눕니다.
1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.
3. 작업을 500번을 반복해도 1이 되지 않는다면 –1을 반환합니다.
"""
# n = 626331
# # result = 4
# cnt=0
# while(n!=1):
#     if n%2==0:
#         n /= 2
#     elif n%2!=0:
#         n = n*3+1
#     if cnt >500:
#         cnt = -1
#         break
#     cnt += 1
# print(cnt)
time = 1
while True:
    time = str(time)
    print(type(time))
    time = int(time)
    time +=1

