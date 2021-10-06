# input = "3 3\n3 1 2\n4 1 4\n2 2 2" #N X M
input = "2 4 \n7 3 1 8\n3 3 3 4" #N X M
# print(input)
a = list(map(int,input.split()))
row = a[0]
col = a[1] # 행의 수
CARD = a[2:]
list_test = [sorted(CARD[i*col:col*(i+1)]) for i in range(row)]
big_number=0
for i in range(row):
    big_number = max(big_number,list_test[i][0])
    # if big_number<list_test[i][0]:
    #     big_number = list_test[i][0]
print(big_number)
# print(list_test[0])
# print(CARD)
