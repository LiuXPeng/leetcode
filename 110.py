# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def getDeep(tree):
            if not tree:
                return 0
            return max(getDeep(tree.left), getDeep(tree.right)) + 1
        if not root:
            return True
        if abs(getDeep(root.left) - getDeep(root.right)) > 1:
            return False
        return (self.isBalanced(root.left) and self.isBalanced(root.right))