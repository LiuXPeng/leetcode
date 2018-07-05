# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        slow = fast = head
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
                slow = slow.next
            else:
                break
        if not slow or not slow.next:
            return
        half = slow.next
        slow.next = None
        pre = half.next
        half.next = None
        while pre:
            temp = pre
            pre = pre.next
            temp.next = half
            half = temp
        tag = head
        while tag.next:
            temp = tag.next
            tag.next = ListNode(half.val)
            tag.next.next = temp
            tag = temp
            half = half.next
            if not half:
                return
        return

#########################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return 
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        
        p = slow.next
        slow.next = None
        node = None
        while p:
            nxt = p.next
            p.next = node
            node = p
            p = nxt
        
        p = head
        while node:
            tmp = node.next
            node.next = p.next
            p.next = node
            p = p.next.next
            node = tmp