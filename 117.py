# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        path = [root]
        while path:
            temp = []
            pre = None
            for cur in path:
                if cur.left:
                    temp.append(cur.left)
                if cur.right:
                    temp.append(cur.right)
                if pre:
                    pre.next = cur
                pre = cur
            path = temp
        return 