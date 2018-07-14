# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        n = len(nums)
        if n == 1:
            return TreeNode(nums[0])
        mid = n // 2
        res = TreeNode(nums[mid])
        res.left = self.sortedArrayToBST(nums[:mid])
        res.right = self.sortedArrayToBST(nums[mid + 1:])
        return res