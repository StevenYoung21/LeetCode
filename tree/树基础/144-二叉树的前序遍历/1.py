class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root) :

        res = []
        def DFS(node):
            if node:
                res.append(node.val)
                DFS(node.left)
                DFS(node.right)

        DFS(root)
            
        return res


root = [1,None,2,3]

c = TreeNode(3,None,None) 
b = TreeNode(2,c,None)
a = TreeNode(1,None,b)

root = a

s1 = Solution()


print(s1.preorderTraversal(root))
# print(t1)
# print_by_layer_2(t1)