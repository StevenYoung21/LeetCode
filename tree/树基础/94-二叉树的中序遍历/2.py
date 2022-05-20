class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root) :

        if not root:
            return []

        res = []
        stack = []
        cur = root

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)   ## 输出结果
                cur = cur.right

        return res


root = [1,None,2,3,4]

d = TreeNode(4,None,None)
c = TreeNode(3,None,None) 
b = TreeNode(2,c,d)
a = TreeNode(1,None,b)

root = a

s1 = Solution()

print(s1.inorderTraversal(root))