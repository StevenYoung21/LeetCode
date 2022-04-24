
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
    def swapPairs(self, head: ListNode) -> ListNode:

        length = 0

        l = head

        while l :
            length += 1
            l = l.next

        if length == 0 or length == 1: return head


        preNode = ListNode(None,head)
        pre = preNode

        cur = preNode

        while cur.next and cur.next.next:
            temp1 = cur.next
            temp2 = cur.next.next.next

            cur.next = cur.next.next
            cur.next.next = temp1
            cur.next.next.next = temp2

            cur = cur.next.next

        
        return pre.next



head = [1,2,3,4,5,6,7]

link1 = create_linked_list(head)


s1 = Solution()

# res = s1.mergeTwoLists(link1,link2)


res=print_linked_list(s1.swapPairs(link1))