# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        sum = sum - root.val
        if root.left == None and root.right == None:
            if sum == 0:
                return True
            return False
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)