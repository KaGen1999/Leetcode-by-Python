# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = ''
        s2 = ''
        while l1 != None:
            s1 = s1 + str(l1.val)
            l1 = l1.next
        while l2 != None:
            s2 = s2 + str(l2.val)
            l2 = l2.next
        s = str(int(s1)+int(s2))
        l = ListNode(s[0])
        head = l
        for i in range(1,len(s)):
            l.next = ListNode(s[i])
            l = l.next
        return head