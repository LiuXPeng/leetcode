class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        res = ListNode(0)
        res.next = head
        tag = res
        for i in range(m - 1):
            tag = tag.next
        end = tag.next
        back = tag.next
        forward = back.next
        temp = tag.next.next
        for i in range(n - m):
            temp = forward.next
            forward.next = back
            back = forward
            forward = temp
        tag.next = back
        end.next = temp
        return res.next   