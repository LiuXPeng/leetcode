# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        def method(m, n):
            if m == n:
                return [None]
            res = []
            for i in range(m, n):
                for j in method(m, i):
                    for k in method(i + 1, n):
                        res.append(TreeNode(i))
                        res[-1].left = j
                        res[-1].right = k
            return res     
        return method(1, n + 1)