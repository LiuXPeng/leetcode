# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head == None:
            return head
        res = pre = head
        if pre.val >= x:
            while pre:
                if pre.next == None:
                    return head
                if pre.next.val >= x:
                    pre = pre.next
                    continue
                res = pre.next
                pre.next = pre.next.next
                res.next = head
                break
        tag = pre
        pre = res
        while tag.next:
            if tag.next.val >= x:
                tag = tag.next
            else:
                if pre == tag:
                    pre = pre.next
                    tag = tag.next
                    continue
                temp = tag.next
                tag.next = tag.next.next
                temp.next = pre.next
                pre.next = temp
                pre = temp
        return res   