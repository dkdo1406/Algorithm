M,D = map(int,input().split())

month_31 = [1,3,5,7,8,10,12]
month_30 = [4,6,9,11]
dayOfTheWeekend = {0: "SUN", 1: "MON", 2: "TUE", 3: "WED", 4: "THU", 5: "FRI", 6: "SAT"}

day = 0
for i in range(1,M):
    if i in month_31:
        day += 31
    elif i in month_30:
        day += 30
    else:
        day += 28

day += D

print(dayOfTheWeekend[day%7])