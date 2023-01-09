import time

start = time.time()
input ="999999999917654521215481 545321213453"
N,K = map(int,input.split())
count = 0

# 처음생각했던 코드
# while N!=1:
#     if N%K==0:
#         N/=K
#     else:
#         N -= 1
#     # print("N : {}, COUNT : {}".format(N,count))
#     count+=1

# 성능 개선 코드 26 5
while True:
    target = (N//K) * K
    count += (N-target)
    N = target
    if N<K:
        break
    count +=1
    N //=K
count += (N-1)



print("time :", time.time() - start)
print(count)
