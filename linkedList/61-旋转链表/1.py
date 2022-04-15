
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

## 创建链表
def create_linked_list(nums):
    if len(nums) == 0:
        return None
    head = ListNode(nums[0])
    cur = head
    for i in range(1, len(nums)):
        cur.next = ListNode(nums[i])
        cur = cur.next
    return head

## 打印链表
def print_linked_list(list_node):
    if list_node is None:
        return

    cur = list_node
    while cur:
        print(cur.val, '->', end=' ')
        cur = cur.next
    print('null')

class Solution:
    def rotateRight(self, head, k: int) :

        ## step1 : 计算链表长度
        cur = head
        length = 0

        while cur:
            length += 1
            cur = cur. next

        ## step2 : 几种特殊情况可以直接返回链表
        if head == None : return None
        if k == 0 : return head   ## k等于0, 不用移动
        if length == 1 or k % length == 0: return head ## 当链表只有一个元素, 或者移动元素个数和链表长度相等, 都相当于没有移动链表.


        ## step3 : 头尾两个串的数量计算 
        tailCount = 0   

        if k > length:
            tailCount = k % length 
        else:
            tailCount = k

        headCount = length - tailCount  
        headCount2 = headCount  ## 头串数量拷贝一份, 这个值要用两次


        ## step4 : cur1 指向尾串 4->5->Null
        cur1 = head

        while headCount:    
            cur1 = cur1.next
            headCount -= 1


        ## step5 : cur2 指向头串, 用headCount2来计数, 使cur2Tail移动到分割点, 令其尾部指向None

        cur2Head = head
        cur2Tail = cur2Head

        while cur2Tail :
            if headCount2 == 1: ## 计数点不是到0, 而是1.  1->2->3->Null, 从 1 移动到 3 只需要移动两个位置.
                cur2Tail.next = None
                break
            else:
                headCount2 -= 1
                cur2Tail = cur2Tail.next


        ## step6 : 移动到 cur1 的最后一个节点, 再与 cur2 进行拼接即可.
        cur1Head = cur1
        while cur1.next:
            cur1 = cur1.next

        cur1.next = cur2Head

        return cur1Head

'''
思路:
存在切割链表的情况下, 最终链表是被分成头尾两部分, 那我们可以把 尾部的链表 与 头部的链表 进行拼接, 得到的就是结果
cur1: 尾部的链表 4->5->Null
cur2: 头部链表   1->2->3->Null

结果: cur1 + cur2, 找的cur1的尾部连接上cur2的头部.


'''


head = [1,2,3,4,5]

k = 1

link1 = create_linked_list(head)

s1 = Solution()

# res = s1.mergeTwoLists(link1,link2)

# print(s1.rotateRight(link1,k))

res=print_linked_list(s1.rotateRight(link1,k))