def lengthOfLIS(nums) -> int:
    sub = []
    for x in nums:
        if len(sub) == 0 or sub[-1] < x:
            sub.append(x)
        else:
            idx = bisect_left(sub, x) # Find the index of the smallest number >= x
            sub[idx] = x # Replace that number with x
    print(sub)
    return len(sub)
def bisect_left(nums, x):
    for i in range(len(nums)):
        if nums[i] >= x:
            return i

nums = [4,10,4,3,1,9]
print(lengthOfLIS(nums))


