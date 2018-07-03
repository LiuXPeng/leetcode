# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        res = ListNode(-float('inf'))
        res.next = head
        pre = head
        tag = head.next
        while tag:
            if tag.val < pre.val:
                pre.next = tag.next
                pre1 = res
                while tag.val > pre1.next.val:
                    pre1 = pre1.next
                tag.next = pre1.next
                pre1.next = tag
                tag = pre.next
                continue
            tag = tag.next
            pre = pre.next
        return res.next