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
    def mergeTwoLists(self, list1 , list2) :

        cur1 = list1
        cur2 = list2

        preNode = ListNode(None,list1)

        pre = preNode
        
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                pre.next = cur1
                cur1 = cur1.next
            else :
                pre.next = cur2
                cur2 = cur2.next
            pre = pre.next

        if cur1 is not None:
            pre.next = cur1

        if cur2 is not None:
            pre.next =cur2

        return preNode.next


l1 = [1,2,4]
l2 = [1,3,4]

link1 = create_linked_list(l1)

link2 = create_linked_list(l2)

s1 = Solution()

# res = s1.mergeTwoLists(link1,link2)

# print(res)

res=print_linked_list(s1.mergeTwoLists(link1,link2))