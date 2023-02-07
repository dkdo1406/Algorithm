from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = 0
        q = []
        dic = defaultdict(int)
        last_index = 0
        for i in range(len(fruits)):
            if fruits[i] not in dic:
                q.append(fruits[i])
            dic[fruits[i]] += 1
            if len(dic) == 2 and fruits[i] != fruits[i-1]:
                last_index = i
            if len(dic) == 3:
                ans = max(ans, dic[q[0]] + dic[q[1]])
                pop_index = 0
                if q[0] == fruits[i-1]:
                    pop_index = q.pop(1)
                else:
                    pop_index = q.pop(0)
                dic.pop(pop_index)
                dic[fruits[i-1]] = i - last_index
                last_index = i
        if len(q) == 1:
            ans = max(ans, dic[q[0]])
        else:
            ans = max(ans, dic[q[0]] + dic[q[1]])
        return ans

