"""
https://programmers.co.kr/learn/courses/30/lessons/12977?language=python3

주어진 숫자 중 서로 다른 3개를 더했을 때 소수가 되는 경우의 개수를 구하라
중복 숫자는 없다.
itertools를 사용하여 combinations를 하면 편하지만 사용못하는 경우를 생각해서 만들어 봄
nums =[1,2,3,4]
answer = 1
"""

nums =[1,2,3,4]
answer = 0
def Prime(nums):
    if nums==1:
        return 0
    for i in range(2,nums):
        if nums%i==0:
            return 0
    return 1

for i in range(len(nums)-2):
    for j in range(i+1,len(nums)-1):
        for k in range(j+1,len(nums)):
            answer +=Prime(nums[i]+nums[j]+nums[k])
            print(nums[i]+nums[j]+nums[k])
print(answer)
