# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        if root.right == None and root.left == None:
            if root.val == sum:
                return [[root.val]]
            else:
                return []
        res = []
        if root.left:
            temp = self.pathSum(root.left, sum - root.val)
            if temp:
                for i in temp:
                    res.append([root.val] + i)
        if root.right:
            temp = self.pathSum(root.right, sum - root.val)
            if temp:
                for i in temp:
                    res.append([root.val] + i)
        return res