# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        loc = [0]
        path = [root]
        while path:
            cur = path.pop()
            cur_loc = loc.pop()
            if cur.left:
                path.append(cur.left)
                loc.append(cur_loc + 1)
            if cur.right:
                path.append(cur.right)
                loc.append(cur_loc + 1)
            if cur_loc >= len(res):
                res.append(cur.val)
        return res