input = 5
x = 59*59
sec = 60
min = 60
hour = 24
tick = 0
for i in range(input+1):
    for j in range(min):
        for k in range(sec):
            if '3' in str(i) + str(j) + str(k):
            # if i or j or k ==3 이건 3일경우에만 ex) 23 33은 못잡음
                tick+=1
print(tick)