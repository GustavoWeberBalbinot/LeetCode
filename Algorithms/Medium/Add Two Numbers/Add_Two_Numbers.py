# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        above = 0
        n = ''
        while (l1 != None or l2 != None):
            num1, num2 = 0, 0
            if l1 != None:
                num1 = l1.val
                l1 = l1.next
            if l2 != None:
                num2 = l2.val
                l2 = l2.next
            s = num1 + num2 + above
            above = 0
            if s >= 10:
                above = 1
                s = s - 10
            if n == '':
                n = ListNode(s)
                h = n
            else:
                h.next = ListNode(s)
                h = h.next
        if above == 1:
            h.next = ListNode(1)
        return n
