# Definition for singly-linked list.
from os import curdir


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        
        if head == None or head.next == None : return False

        dis = []

        cur = head

        while cur :
            if cur in dis:
                return True
            else:
                dis.append(cur)
            cur = cur.next
        return False


        