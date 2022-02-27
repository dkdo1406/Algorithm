input = 123402
number = str(input)
number_L = number[:(len(number))//2]
number_R = number[(len(number))//2:]
result = 0
for i in range((len(number))//2):
    result += int(number_L[i])-int(number_R[i])
if result==0:
    print("LUCKY")
else:
    print("READY")
