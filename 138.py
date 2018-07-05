# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return
        tag = head
        while tag:
            temp = tag.next
            new = RandomListNode(tag.label)
            tag.next = new
            new.next = temp
            tag = temp
        tag = head
        while tag:
            if tag.random:
                tag.next.random = tag.random.next
            tag = tag.next.next
        res = head.next
        tag = head
        while tag and tag.next:
            temp = tag.next
            tag.next = tag.next.next
            tag = temp
        return res