
## 链表相关操作

## 链表结点定义
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


nums = [1,2,3]

link = create_linked_list(nums)

print_linked_list(link)