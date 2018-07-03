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
        if not head:
            return
        label = head.val
        temp = head
        while temp.next:
            if temp.next.val == label:
                temp.next = temp.next.next
            else:
                temp = temp.next
                label = temp.val
        return head