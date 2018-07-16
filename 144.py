# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        L = [root]
        res = []
        while L:
            cur = L.pop()
            if cur:
                res.append(cur.val)
                L.append(cur.right)
                L.append(cur.left)
        return res