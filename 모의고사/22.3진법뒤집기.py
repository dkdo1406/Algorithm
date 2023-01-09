n = 125
ternary_list = []
answer = 0
tmp=''
while n:
    ternary_list.append(n%3)
    tmp+=str(n%3)
    n //=3

ternary = int(''.join(list(map(str,ternary_list))))
count = 0
print(int(tmp,3))
while(ternary>0):
    if ternary>=10:
        answer += (ternary%10)*(3**count)
    else:
        answer += ternary*(3**count)
    ternary //=10
    count +=1
print(answer)




