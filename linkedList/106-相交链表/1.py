
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        cur1 = headA
        cur2 = headB

        if cur1 == None or cur2 == None : return None

        while cur1 is not cur2 :
            if cur1 :
                cur1 = cur1.next
            else:
                cur1 = headB
            if cur2 :
                cur2 = cur2.next
            else:
                cur2 = headA
        
        return cur1


