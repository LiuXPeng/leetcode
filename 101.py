# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def method(loc1, loc2):
            if (not loc1) and (not loc2):
                return True
            if not (loc1 and loc2):
                return False
            if loc1.val != loc2.val:
                return False
            return method(loc1.left, loc2.right) and method(loc1.right, loc2.left)
        return method(root.left, root.right)
        #return method(root, root)