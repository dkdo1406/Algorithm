class SmallestInfiniteSet:

    def __init__(self):
        self.i = 1
        self.heap = []
        self.check = set()
        

    def popSmallest(self) -> int:
        if self.heap:
            tmp = heapq.heappop(self.heap)
            if self.i > tmp:
                self.check.remove(tmp)
                return tmp
            heapq.heappush(self.heap, tmp)            
        self.i += 1
        return self.i - 1
            
        

    def addBack(self, num: int) -> None:
        if num < self.i and num not in self.check:
            heapq.heappush(self.heap, num)
            self.check.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)