class SummaryRanges:

    def __init__(self):
        global arr
        dic = dict()
        arr = []

    def addNum(self, value: int) -> None:
        global arr
        if value not in arr:
            arr.append(value)
            arr.sort()

    def getIntervals(self) -> List[List[int]]:
        global arr
        answer = []
        cnt = -1
        temp_arr = []
        for i in range(len(arr)):
            if arr[i] != cnt:
                if temp_arr:
                    temp_arr.append(cnt-1)
                    answer.append(temp_arr)
                    temp_arr = []
                cnt = arr[i]
                temp_arr.append(cnt)
                
            cnt += 1
        temp_arr.append(cnt-1)
        answer.append(temp_arr)

        return answer


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()