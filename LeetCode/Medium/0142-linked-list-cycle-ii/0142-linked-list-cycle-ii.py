# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        check = set()
        while True:
            if head is None or head.next is None:
                return
            if head in check:
                return head
            check.add(head)
            head = head.next
        return