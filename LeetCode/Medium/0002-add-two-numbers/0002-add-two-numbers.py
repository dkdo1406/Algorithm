# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        global ans
        ans = 0
        L = 1
        if l1.next == None:
            ans += l1.val
        if l2.next == None:
            ans += l2.val
        while l1.next != None or l2.next != None:
            if l1.next != None:
                ans += l1.val * L
                l1 = l1.next
                if l1.next == None:
                    ans += l1.val * 10 * L
            if l2.next != None:
                ans += l2.val * L
                l2 = l2.next
                if l2.next == None:
                    ans += l2.val * 10 * L
            L *= 10

        root = l3 = ListNode()
        ListNode_temp = list(map(int, reversed(str(ans))))

        for i in ListNode_temp:
            l3.next = ListNode(i)
            l3 = l3.next
        return root.next