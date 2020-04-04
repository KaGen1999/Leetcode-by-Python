# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = ListNode(0)
        p = l
        while True:
            if l2 == None:
                p.next = l1
                break
            if l1 == None:
                p.next = l2
                break
            if l1.val < l2.val:
                p.next = ListNode(l1.val)
                p = p.next
                l1 = l1.next
            else:
                p.next = ListNode(l2.val)
                p = p.next
                l2 = l2.next
        return l.next