# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        node = head
        self.arr = []
        while node is not None:
            self.arr.append(node.val)
            node = node.next
        

    def getRandom(self) -> int:
        return random.choice(self.arr)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()