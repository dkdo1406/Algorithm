"""
https://leetcode.com/problems/product-of-array-except-self/
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
nums[i]를 제외한 나머지 값들의 곱을 output[i]에 저장
나눗셈 사용않고 O(n)으로 구해라
"""
nums = [1,2,3,4]
answer = []
p=1
for i in range(len(nums)):
    # i를 뺸 나머지에 i를 곱한다.
    answer.append(p)
    p = p * nums[i]
p=1
for i in range(len(nums)-1,-1,-1):
    answer[i] = answer[i]*p
    p = p * nums[i]
print(answer)
