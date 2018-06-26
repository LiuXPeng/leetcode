# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None
        node = TreeNode(postorder[-1])
        for i in range(len(inorder)):
            if inorder[i] == node.val:
                break
        node.left = self.buildTree(inorder[0:i], postorder[0:i])
        node.right = self.buildTree(inorder[i + 1:], postorder[i:len(postorder) - 1])
        return node