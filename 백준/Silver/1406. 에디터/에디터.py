import sys
input = lambda : sys.stdin.readline()
N = input()
M = int(input())
dic = dict()
class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
class DLinkedList:
    def __init__(self):
        self.head = LinkedList("start")
        self.cnt = 0
    def addVal(self, val):
        new_node = LinkedList(val)
        self.head.next = new_node
        new_node.prev = self.head
        self.head = self.head.next
        self.cnt += 1

    def insert(self, val):
        new_node = LinkedList(val)
        if self.head.prev == None:
            self.head.next.prev = new_node
            new_node.next = self.head.next
            self.head.next = new_node
            new_node.prev = self.head
            self.head = self.head.next
            return
        if self.head.next == None:
            self.head.next = new_node
            new_node.prev = self.head
            self.head = self.head.next
            return
        self.head.next.prev = new_node
        new_node.next = self.head.next
        self.head.next = new_node
        new_node.prev = self.head
        self.head = self.head.next

    def moveLeft(self):
        if self.head.prev == None or self.head == None:
            return
        else:
            self.head = self.head.prev

    def moveRight(self):
        if self.head == None or self.head.next == None:
            return
        else:
            self.head = self.head.next
    def deleteLeft(self):
        if self.head.prev == None or self.head == None:
            return
        if self.head.next == None:
            self.head.prev.next = self.head.next
            self.head = self.head.prev
            return
        self.head.prev.next = self.head.next
        self.head.next.prev = self.head.prev
        self.head = self.head.prev

def printLink(link):
    while link != None:
        print(link.val, end= ' ')
        link = link.prev

def printAns(link):
    while link.prev != None:
        link = link.prev
    if link.val == "start":
        link = link.next
    # print(link.next.val)
    while link != None:
        print(link.val, end ='')
        link = link.next

link = DLinkedList()
for i in N:
    if i == '\n':
        break
    link.addVal(i)
# printLink(link.head)

for _ in range(M):
    order = input().split()
    #왼쪽 추가
    if order[0] == 'P':
        link.insert(order[1])
        pass
    #왼쪾 이동
    elif order[0] == 'L':
        link.moveLeft()

    # 오른쪽 이동
    elif order[0] == 'D':
        link.moveRight()
    #왼쪽 삭제
    elif order[0] == 'B':
        link.deleteLeft()

printAns(link.head)