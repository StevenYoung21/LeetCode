# Definition for singly-linked list.
from os import curdir


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        
        if head == None or head.next == None : return False

        fast , slow = head, head

        while fast != None and fast.next != None :  ## fast每次走两步,所以要提前判断不能为空
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False  



        