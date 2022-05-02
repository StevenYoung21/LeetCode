class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


## 构建二叉树
class Tree(object):
    """树类"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def add(self, val):
        """为树添加节点"""
        node = TreeNode(val)
        #如果树是空的，则对根节点赋值
        if self.root == None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            #对已有的节点进行层次遍历
            while queue:
                #弹出队列的第一个元素
                cur = queue.pop(0)
                if cur.left == None:
                    cur.left = node
                    return
                elif cur.right == None:
                    cur.right = node
                    return
                else:
                    #如果左右子树都不为空，加入队列继续判断
                    queue.append(cur.left)
                    queue.append(cur.right)

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

t1 = Tree(root)

s1 = Solution()


print(s1.preorderTraversal(t1))

# print_by_layer_2(t1)