absolutes = [4,7,12]
signs = [True,False,True]
answer = 0
for a,b in zip(absolutes,signs):
    if b == False:
        a= -a
    answer +=a
print(answer)