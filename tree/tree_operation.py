
## 树相关操作

## 树结点定义
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


## 打印二叉树
def print_by_layer_2(root):
    ''' 
    3. 终极版
    无line/current_line,在入队时候加入换行标记信息，注意边界条件，防止陷入死循环
    '''
    if not root:
        return 
    queue = ["r"] # 一开始塞入一个换行标记，作为队首,任何非TreeNode对象都行。
    queue.append(root)
    while len(queue) > 0:
        node = queue.pop(0)
        if isinstance(node,Tree):
            print(node.elem, end = " ")
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)
        else:
            # 边界条件
            if len(queue) > 0:
                queue.append("r") # 对尾添加换行标记
                print()  # 换行
