# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        res = ListNode(-float('inf'))
        res.next = head
        pre = res
        back = res.next
        forward = res.next.next
        while forward:
            if back.val != forward.val:
                pre = back
                back = forward
                forward = forward.next
            else:
                while forward and forward.val == back.val:
                    forward = forward.next
                pre.next = forward
                if not pre.next:
                    break
                back = pre.next
                forward = back.next
        return res.next   