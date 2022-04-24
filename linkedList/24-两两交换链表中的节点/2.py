
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



        preNode = ListNode(None,head)
        pre = preNode

        while pre.next and pre.next.next:
            cur = pre.next
            post = pre.next.next

            cur.next = post.next
            post.next = cur
            pre.next = post

            pre = pre.next.next

        
        return preNode.next



head = [1,2,3,4,5,6,7]

link1 = create_linked_list(head)


s1 = Solution()

# res = s1.mergeTwoLists(link1,link2)


res=print_linked_list(s1.swapPairs(link1))