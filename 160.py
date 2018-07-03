# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not (headA and headB):
            return
        A = headA
        B = headB
        countA = countB = 0
        while A:
            countA += 1
            A = A.next
        while B:
            countB += 1
            B = B.next
        A = headA
        B = headB
        if countA > countB:
            for i in range(countA - countB):
                A = A.next
        else:
            for i in range(countB - countA):
                B = B.next
        while A:
            if A == B:
                return A
            A = A.next
            B = B.next
        return


##########
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        trav_a, trav_b = headA, headB
        while trav_a is not trav_b:
            trav_a = headB if not trav_a else trav_a.next
            trav_b = headA if not trav_b else trav_b.next
        return trav_a