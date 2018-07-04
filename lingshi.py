# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return
        tag = head
        count = 1  # 让count多一个
        while tag:
            tag = tag.next
            count += 1
        if count == 2:
            return TreeNode(head.val)
        if count == 3:
            res = TreeNode(head.next.val)
            res.left = TreeNode(head.val)
            return res
        k = count // 2
        tag = head
        for i in range(0, k - 2):
            tag = tag.next
        temp = tag.next
        res = TreeNode(temp.val)
        tag.next = None
        res.left = self.sortedListToBST(head)
        res.right = self.sortedListToBST(temp)
        return res


def stringToIntegerList(input):
    return json.loads(input)


def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def treeNodeToString(root):
    return "[" + output[:-2] + "]"


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            head = stringToListNode(line);

            ret = Solution().sortedListToBST(head)

            out = treeNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()