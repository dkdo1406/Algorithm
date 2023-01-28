from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict(list)
        answer = []
        for i in range(len(nums)):
            dic[nums[i]] += [i]
        for i in range(len(nums)):
            if target - nums[i] == nums[i]:
                if len(dic[nums[i]]) == 1:
                    continue
                arr = dic[nums[i]]
                answer.append(arr[0])
                answer.append(arr[1])
                break
            else:
                if dic[target - nums[i]]:
                    answer.append(i)
                    answer.append(dic[target - nums[i]][0])
                    answer.sort()
                    break
        return answer