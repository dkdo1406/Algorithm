"""
https://leetcode.com/problems/3sum/
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

"""
import collections
nums = [-1,0,1,2,-1,-4]

nums.sort()
answer = []
for i in range(len(nums) - 2):
    #중복값 넘기기
    if i > 0 and nums[i] == nums[i - 1]:
        continue
    sum = 0
    lt = i + 1
    rt = len(nums) - 1
    while lt < rt:
        sum = nums[i] + nums[lt] + nums[rt]
        if sum < 0:
            lt += 1
        elif sum > 0:
            rt -= 1
        # sum이 정답일 경우 어떻게 할 것인가
        if sum == 0:
            answer.append([nums[i], nums[lt], nums[rt]])
            if lt < rt and nums[lt] == nums[lt + 1]:
                lt += 1
            while lt < rt and nums[rt] == nums[rt - 1]:
                rt -= 1
            lt += 1
            rt -= 1
print(nums)
print(answer)