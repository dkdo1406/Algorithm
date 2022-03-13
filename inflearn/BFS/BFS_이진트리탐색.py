import collections
class Node:
    def __init__(self,item):
        self.item = item
        self.left = None
        self.right = None
class BinaryTree():
    def __init__(self):
        self.root = None
tree = BinaryTree()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)
n10 = Node(10)
n11 = Node(11)
tree.root=n1
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n4.left = n8
n5.right = n9
n9.left = n10
n6.right = n11
def BFS(root):
    q = collections.deque()
    q.append(root)
    L=0
    while q:
        print(L,": ",end='')
        for i in range(len(q)):
            cur = q.popleft()
            print(cur.item,end=' ')
            if cur.left!=None:
                q.append(cur.left)
            if cur.right!=None:
                q.append(cur.right)
        L+=1
        print()

BFS(tree.root)