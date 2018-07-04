# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        if not head.next:
            return head
        slow = head
        fast = head.next
        while fast:
            fast = fast.next
            if not fast:
                break           
            fast = fast.next
            slow = slow.next
        B = self.sortList(slow.next)
        slow.next = None
        A = self.sortList(head)
        res = ListNode(0)
        tag = res
        while A and B:
            if A.val < B.val:
                tag.next = A
                tag = A
                A = A.next
            else:
                tag.next = B
                tag = B
                B = B.next
        if A:
            tag.next = A
        if B:
            tag.next = B
        return res.next