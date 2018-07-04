# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return
        tag = head
        count = 1 #让count多一个
        while tag:
            tag = tag.next
            count += 1
        if count == 2:
            return TreeNode(head.val)
        if count == 3:
            res = TreeNode(head.next.val)
            res.left = TreeNode(head.val)
            return res
        k = count // 2
        tag = head
        for i in range(0, k - 2):
            tag = tag.next
        temp = tag.next
        res = TreeNode(temp.val)
        tag.next = None
        res.left = self.sortedListToBST(head)
        res.right = self.sortedListToBST(temp.next)
        return res