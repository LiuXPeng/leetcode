# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root, n = 0):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        path = [root]
        res = 0
        value = {root:0}
        while path:
            cur = path.pop()
            temp = value.get(cur) * 10 + cur.val
            if cur.left == None and cur.right == None:
                res = res + temp
            if cur.left:
                value[cur.left] = temp
                path.append(cur.left)
            if cur.right:
                value[cur.right] = temp
                path.append(cur.right)
        return res