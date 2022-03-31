"""
케익상자의 숫자가 7,11,17의 조합이 맞을경우 먹을 수 있다.
입력하는 케익상자는 먹을 수 있을까?
"""
cake = 5730154
chk_list = [False]*10000001
list_3 = [553,757,901]
for i in list_3:
    chk_list[i]=True
for i in range(18,cake+1):
    if chk_list[i-list_3[0]] or chk_list[i-list_3[1]] or chk_list[i-list_3[2]]:
        chk_list[i]=True
print(chk_list[cake])


