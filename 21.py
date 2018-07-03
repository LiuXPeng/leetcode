# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        res = tag1 = l1
        tag2 = l2
        if l1.val > l2.val:
            res = l2
            tag2 = tag2.next
        else:
            tag1 = tag1.next
        temp = res
        while tag1 and tag2:
            if tag1.val > tag2.val:
                temp.next = tag2
                temp = temp.next
                tag2 = tag2.next
            else:
                temp.next = tag1
                temp = temp.next
                tag1 = tag1.next
        if tag1:
            temp.next = tag1
        else:
            temp.next = tag2
        return res