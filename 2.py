# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        res = l1
        label = 0
        pre = l1
        while l1 and l2:
            l1.val = l1.val + l2.val + label
            if l1.val >= 10:
                l1.val -= 10
                label = 1
            else:
                label = 0
            pre = l1
            l1 = l1.next
            l2 = l2.next
        if l2:
            pre.next = l2
            l1 = l2
        while l1:
            l1.val = l1.val + label
            if l1.val >= 10:
                l1.val -= 10
                label = 1
            else:
                label = 0
            pre = l1
            l1 = l1.next
        if label == 1:
            pre.next = ListNode(1)
        return res