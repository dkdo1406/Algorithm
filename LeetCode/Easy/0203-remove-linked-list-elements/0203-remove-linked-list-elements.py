# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class SLinkedListNode:
    def __init__(self, val):
        self.__val = val
        self.head = None

    def addHead(self, nodes):
        self.head = nodes

    def addTemp(self, number):
        node = ListNode(number)
        node.next = self.head
        self.head = node
    def delete(self, node):
        if node is None:
            return
        next_node = self.delete(node.next)
        if node.val == self.__val:
            return next_node
        else:
            node.next = next_node
            return node

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        slist = SLinkedListNode(val)
        slist.addHead(head)
        slist.addTemp(-1)
        slist.delete(slist.head)
        return slist.head.next

        