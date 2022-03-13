"""

26일경우
2 + 6 = 8
새로운 숫자 68
6+8=14
새로운숫자 84
반복
앞자리와 뒷자리를 더한다.
뒷자리*10+ 더한숫자
한자리수이면 앞에 0을 붙인다.
"""
N = int(input())
M=N
cnt=1

if M==0:
    pass
else:
    if M < 10:
        M = M*10+M
    else:
        M = (M % 10)*10 + (M // 10 + M % 10) % 10
    while M!=N:
        cnt+=1
        if M<10:
            M = M*10+M
        else:
            M=(M%10)*10+(M%10+M//10)%10
print(cnt)