# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head
        count = 1
        tag = head
        while tag.next:
            count += 1
            tag = tag.next
        tag.next = head
        k = count - k % count
        for i in range(k):
            tag = tag.next
        res = tag.next
        tag.next = None
        return res