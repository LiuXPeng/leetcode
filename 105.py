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
        if len(preorder) == 0:
            return None
        node = TreeNode(preorder[0])
        for i in range(len(inorder)):
            if inorder[i] == node.val:
                break
        node.left = self.buildTree(preorder[1:i + 1], inorder[0:i])
        node.right = self.buildTree(preorder[i + 1:], inorder[i + 1:])
        return node