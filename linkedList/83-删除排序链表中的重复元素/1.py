
# Definition for singly-linked list.
from lib2to3.pytree import Node


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
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        preNode = ListNode(None,head)
        pre = preNode

        cur = head


        while cur and cur.next:
            if cur.val == cur.next.val:
                pre.next = cur.next
            else:
                pre = pre.next

            cur = cur.next

        return preNode.next

head = [1,1,2,3]

link = create_linked_list(head)

s1 = Solution()

print_linked_list(s1.deleteDuplicates(link))