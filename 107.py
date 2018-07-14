# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        node = [[root]]
        temp = node[-1]
        res = [[root.val]]
        while len(temp) != 0:
            node.append([])
            res.insert(0, [])
            for i in temp:
                if i.left:
                    node[-1].append(i.left)
                    res[0].append(i.left.val)
                if i.right:
                    node[-1].append(i.right)
                    res[0].append(i.right.val)
            temp = node[-1]
        return res[1:]
        '''
        for i in range(len(node) - 2, -1, -1):
            res.append([])
            for j in node[i]:
                res[-1].append(j.val)
        return res
        '''