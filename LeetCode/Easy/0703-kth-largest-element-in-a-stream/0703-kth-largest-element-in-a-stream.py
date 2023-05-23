class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        heapq.heapify(self.nums)
        if k <= len(self.nums):
            for _ in range(len(nums) - k):
                heapq.heappop(self.nums)
            self.k = heapq.heappop(self.nums)
        else:
            self.k = -10 ** 5

    def add(self, val: int) -> int:
        if self.k < val:
            heapq.heappush(self.nums, val)
            self.k = heapq.heappop(self.nums)
        return self.k
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)