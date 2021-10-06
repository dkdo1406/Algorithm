a= 5
b = 1

mon_31 = [1,3,5,7,8,10,12]
mon_30 = [4,6,9,11]
mon_29 = [2]
answer = ''
week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
day = 0
for month in range(a):
    if month + 1 == a:
        break
    elif month+1 in mon_29:
        day += 29
    elif month + 1 in mon_30:
        day += 30
    elif month + 1 in mon_31:
        day += 31

answer = week[(day + b - 1) % 7]
print(day + b - 1)
# print(answer)