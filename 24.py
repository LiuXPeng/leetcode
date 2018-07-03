# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        res = head.next
        pre = head
        head.next = res.next
        res.next = head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            a.next = b.next
            b.next = a
            pre.next = b
            pre = a
        return res