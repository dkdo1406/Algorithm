"""
https://leetcode.com/problems/trapping-rain-water/
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

"""
# 스택
height = [0,1,0,2,1,0,1,3,2,1,2,1]
for i in range(len(height)-1):
    height[i]
exit()
#  투포인터
height = [0,1,0,2,1,0,1,3,2,1,2,1]
lt = 0
rt = len(height)-1
lt_max, rt_max = height[lt],height[rt]
volume = 0
while lt<rt:
    lt_max = max(height[lt],lt_max)
    rt_max = max(height[rt],rt_max)
    if height[lt]<=height[rt]:
        volume += lt_max - height[lt]
        print(lt, lt_max, volume)
        lt+=1

    else:
        volume += rt_max - height[rt]
        rt -= 1


