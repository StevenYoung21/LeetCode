class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root) :

        if not root:
            return []

        res = []

        stack = [root]

        while stack:
            node = stack.pop()

            res.append(node.val)
            
            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return res[::-1]


root = [1,None,2,3,4]

d = TreeNode(4,None,None)
c = TreeNode(3,None,None) 
b = TreeNode(2,c,d)
a = TreeNode(1,None,b)

root = a

s1 = Solution()

print(s1.postorderTraversal(root))