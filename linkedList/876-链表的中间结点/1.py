# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

        k = 0

        probe = head
        while( probe != None ):
            probe = probe.next
            k = k + 1

            index = k//2 +1

        resLink = head
        while( index > 1 ):
            resLink = resLink.next
            index = index - 1

        return index

link6 = ListNode(6,None)
link5 = ListNode(5,link6)
link4 = ListNode(4,link5)
link3 = ListNode(3,link4)
link2 = ListNode(2,link3)
link1 = ListNode(1,link2)

s1 = Solution()

res = s1.middleNode(link1)


print(res)

# print(link5.next)
