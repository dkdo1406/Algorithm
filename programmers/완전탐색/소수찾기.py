"""
https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3

numbers	return
"17"	3
"011"	2
예제 #1
[1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.
예제 #2
[0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.
11과 011은 같은 숫자로 취급합니다.
"""

numbers = "17"
answer=0

lst = list(numbers)
print(lst)

result=[]
def Prime(num):
    if num==0 or num==1:
        return 0
    for i in range(2,num):
        if num%i==0:
            return 0
    return 1


def permutation(arr,r):
    result = []
    def permute(p, index):
        if len(p) ==r:
            result.append(p)
            return
        for idx, data in enumerate(arr):
            if idx not in index:
                permute(p + [data], index + [idx])

    permute([],[])

    return result
        

# for i in range(1,len(numbers)+1):
for combi in permutation("",numbers):
    print(combi)
    result.append(int(''.join(combi)))
result = set(result)

for i in result:
    answer +=Prime(i)


