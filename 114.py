# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        res = []
        path = [root]
        while path:
            cur = path.pop()
            res.append(cur)
            if cur.right:
                path.append(cur.right)
            if cur.left:
                path.append(cur.left)
        for i in range(len(res) - 1):
            res[i].left = None
            res[i].right = res[i + 1]
        return