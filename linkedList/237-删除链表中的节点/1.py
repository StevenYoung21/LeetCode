# Definition for singly-linked list.
from tkinter import W


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):

        cur = node

        cur.val = cur.next.val
        cur.next = cur.next.next

