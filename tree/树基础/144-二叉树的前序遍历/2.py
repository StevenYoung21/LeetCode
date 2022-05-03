class BiTreeNode:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None

a = BiTreeNode("A")
b = BiTreeNode("B")
c = BiTreeNode("C")
d = BiTreeNode("D")
e = BiTreeNode("E")
f = BiTreeNode("F")
g = BiTreeNode("G")

e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f

root = e


def pre_order(root):
    if root:
        print(root.data, end=',')
        pre_order(root.lchild)
        pre_order(root.rchild)

# pre_order(root)

class Solution:
    def preorderTraversal(self, root) :

        res = []
        def DFS(node):
            if node:
                res.append(node.data)
                DFS(node.lchild)
                DFS(node.rchild)

        DFS(root)
            
        return res

s1 = Solution()

print(s1.preorderTraversal(e))