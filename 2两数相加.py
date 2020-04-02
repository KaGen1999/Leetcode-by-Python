# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a1 = []
        a2 = []
        while True:
            if l1 != None:
                a1.append(l1.val)
                l1 = l1.next
            if l2 != None:
                a2.append(l2.val)
                l2 = l2.next
            if l2 == None and l1 == None:
                break
        s1 = ''
        s2 = ''
        # print(a1,a2)
        if a1 == []:
            s1 = '0'
        else:
            for each in a1:
                s1 = s1 + str(each)
        if a2 == []:
            s2 = '0'
        else:
            for each in a2:
                s2 = s2 + str(each)
        # print(s1,s2)
        s = int(s1[::-1]) + int(s2[::-1])
        s = list(str(s))
        l3 = ListNode()
        for each in s:
            l3.val = int(each)
            l = ListNode()
            l.next = l3
            l3 = l
        return l3.next
