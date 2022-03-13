"""
Y요금제 30초마다 10원
M요금제 60초마다 15원
같으면 이렇게 출력
Y M 가격
3
40 40 40
"""
import math
T = int(input())
lst = map(int,input().split())

Y_charge=0
M_charge=0
for i in lst:
    if i%30==0:
        Y_charge+=10
    if i%60==0:
        M_charge+=15
    Y_charge+= math.ceil(i/30)*10
    M_charge += math.ceil(i / 60) * 15

if Y_charge==M_charge:
    print('Y','M',Y_charge)
elif Y_charge<M_charge:
    print('Y',Y_charge)
else:
    print('M',M_charge)

