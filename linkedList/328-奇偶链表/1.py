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
    def oddEvenList(self, head: ListNode) -> ListNode:

        if head == None  : return None

        if head.next == None : return head

        oddHead = head
        evenHead = head.next

        odd = oddHead

        even = evenHead

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = evenHead
        return oddHead



    



head = [1,2,3,4,5]

link = create_linked_list(head)

s1 = Solution()

res=print_linked_list(s1.oddEvenList(link))