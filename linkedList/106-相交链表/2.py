

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        cur1 = headA
        cur2 = headB

        if cur1 == None or cur2 == None : return None

        dis1 = 0
        dis2 = 0

        while cur1 :
            cur1 = cur1.next
            dis1 += 1
        
        while cur2:
            cur2 = cur2.next
            dis2 += 1

        cur1 = headA
        cur2 = headB

        if dis1 > dis2:
            dis3 = dis1 - dis2
            while dis3 and cur1 :
                cur1 = cur1.next
                dis3 -= 1
        else:
            dis3 = dis2 - dis1
            while dis3 and cur2:
                cur2 = cur2.next
                dis3 -= 1

        while cur1 :
            if cur1 == cur2:
                return cur1
            else:
                cur1 = cur1.next
                cur2 = cur2.next
        
        return None
