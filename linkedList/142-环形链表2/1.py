
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        if head == None : return None

        if head.next == head : return head

        dis = set()

        cur = head


        while cur :
            if cur not in dis:
                dis.add(cur)
                cur = cur.next
            else:
                return cur
                