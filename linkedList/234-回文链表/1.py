# Definition for singly-linked list.
from tkinter.tix import Tree


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
    def isPalindrome(self, head: ListNode) -> bool:

        cur = head

        dis = []

        while cur :
            dis.append(cur.val)
            cur = cur.next

        l , r = 0 , len(dis) - 1

        while(l<=r):
            if dis[l] != dis[r]:
                return False
            else:
                l += 1
                r -= 1

        return True


head = [1,2,2,3,1]

linked = create_linked_list(head)

s1 = Solution()

# print_linked_list(s1.isPalindrome(linked))
print(s1.isPalindrome(linked))