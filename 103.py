# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        path = [root]
        label = True
        res = []
        while path:
            res.append([])
            if label:
                label = False
                for i in path:
                    res[-1].append(i.val)
            else:
                label = True
                for i in range(len(path) - 1, - 1, -1):
                    res[-1].append(path[i].val)
            temp = []
            for i in path:
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            path = temp
        return res