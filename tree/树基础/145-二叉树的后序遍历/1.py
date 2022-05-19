class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root) :

        res = []

        def DFS(root):
            if root:
                DFS(root.left)
                DFS(root.right)
                res.append(root.val)

        DFS(root)

        return res

root1 = [1,None,2,3]

c = TreeNode(3,None,None) 
b = TreeNode(2,c,None)
a = TreeNode(1,None,b)


s1 = Solution()

print(s1.postorderTraversal(a))
