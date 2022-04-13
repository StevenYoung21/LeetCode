# Definition for singly-linked list.
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
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        preNode = ListNode(None,head)
        pre = preNode
        cur = head

        while cur:
            if cur.val == val :
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next

        return preNode.next


head = [7,7,7]
val = 7

link = create_linked_list(head)

s1 = Solution()

res=print_linked_list(s1.removeElements(link,val))
