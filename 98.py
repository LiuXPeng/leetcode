# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        path = [root]
        pre = -float('inf')
        while root:
            while path[-1].left:
                path.append(path[-1].left)
            while not path[-1].right:
                cur = path.pop()
                if cur.val <= pre:
                    return False
                pre = cur.val
                if not path:
                    return True
            cur = path.pop()
            if cur.val <= pre:
                return False
            pre = cur.val
            path.append(cur.right)
        return 

#====================非递归中序遍历===================
def inOrder(self, root):
    if root == None:
        return
    myStack = []
    node = root
    while node or myStack:
        while node:
            # 从根节点开始，一直找它的左子树
            myStack.append(node)
            node = node.lchild
        # while结束表示当前节点node为空，即前一个节点没有左子树了
        node = myStack.pop()
        print node.val
        # 开始查看它的右子树
        node = node.rchild