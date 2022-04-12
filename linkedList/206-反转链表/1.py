# Definition for singly-linked list.
from asyncio.windows_events import NULL
from xml.dom.minicompat import NodeList


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

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def addAtHead(self, val: int) -> None:
        curNode = ListNode(val)  ## 定义当前插入节点
        if self.size == 0:
            self.head = curNode
            self.size += 1
            return
        else:
            curNode.next = self.head
            self.head = curNode
            self.size += 1
            return

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if head == [] : return []

        cur = head 

        s1 = MyLinkedList()

        while cur:    
            s1.addAtHead(cur.val)
            cur = cur.next

        return s1.head

head = [1,2,3,4,5]

link = create_linked_list(head)

s1 = Solution()

res=print_linked_list(s1.reverseList(link))
