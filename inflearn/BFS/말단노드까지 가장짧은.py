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
tree.root = n1
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
def BFS(L,root):
    q = collections.deque()
    q.append(root)
    while q:
        for _ in range(len(q)):
            V= q.popleft()
            if V.left==None and V.right==None:
                return L
            if V.left!=None:
                q.append(V.left)
            if V.right!=None:
                q.append(V.right)
        L+=1

def DFS(L,root): # root가 가리키는게 말단 노드면 L을 리턴
    if root.left==None and root.right==None:
        return L
    else:
        return min(DFS(L+1,root.left),DFS(L+1,root.right)) # 둘중에 작은것을 리턴받아 다시 올라감

print(DFS(0,tree.root))
print(BFS(0,tree.root))

