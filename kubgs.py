# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def method(mid, right, left):
            node = TreeNode(inorder[mid])
            index = 0
            for i in range(right, left):
                if preorder[i] == inorder[mid]:
                    index = i
                    break
            node.left = method(mid + 1, right, index - 1)
            node.left = method(mid + index, index + 1, left)
        res = method(0, 0, len(inorder))
        return res