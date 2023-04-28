class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        
        ans = 0
        n = len(strs[0])
        q = deque()
        strs = set(strs)
        
        while strs:
            q.append(strs.pop())
            while q:
                str_1 = q.popleft()
                if not strs:
                    return ans + 1

                list_strs = list(strs)
                
                for str_2 in list_strs:
                    cnt = 0
                    for k in range(n):
                        if str_1[k] != str_2[k]:
                            cnt += 1
                            if cnt > 2:
                                break
                    if cnt == 2:
                        q.append(str_2)
                        strs.remove(str_2)
            ans += 1

        return ans
