"""
https://leetcode.com/problems/array-partition-i/
Input: nums = [1,4,3,2]
Output: 4
1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4.
배열에 있는 모든 값을 2개씩 묶어 두개 중 작은 값을 모두 더한 값들중 가장 큰값을 출력하라
"""
nums = [6,2,6,5,1,2]
nums.sort()
answer = 0
for i in range(0,len(nums),2):
    answer += nums[i]
    """
    while nums:
    #Runtime: 344 ms
    # Memory Usage: 16.2 MB
    # answer += min(nums.pop(),nums.pop())
    
    # min을 안쓰면 더 빠르지 않을까?
    # Runtime: 521 ms
    # Memory Usage: 16.1 MB
    nums.pop()
    answer += nums.pop()
    """
print(answer)