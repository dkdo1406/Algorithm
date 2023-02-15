class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:  
        num.reverse()
        list_k = list(map(int, str(k)))
        list_k.reverse()
        cnt = 0
        if len(num) < len(list_k):
            num, list_k = list_k, num
        while cnt < len(num):
            if cnt < len(list_k):
                num[cnt] += list_k[cnt]
            if num[cnt] > 9:
                num[cnt] -= 10
                if len(num) <= cnt + 1:
                    num.append(1)
                else:
                    num[cnt + 1] += 1
            cnt += 1
        num.reverse()
        return num
            