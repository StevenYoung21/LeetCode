
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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        
        preNode  = ListNode(None,head)
        pre = preNode

        slow = pre
        fast = pre.next


        while n :
            fast = fast.next
            n -= 1

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next


        return pre.next

    



head = [1,2,3,4,5]
n = 2

link = create_linked_list(head)

s1 = Solution()

res=print_linked_list(s1.removeNthFromEnd(link,n))
# res = print(s1.removeNthFromEnd(link,n))
