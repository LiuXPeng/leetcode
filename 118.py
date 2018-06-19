class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        res = [[1]]
        pre = [1]
        for i in range(2, numRows + 1):
            add = [1]
            for x in range(i - 2):
                add.append(pre[x] + pre[x + 1])
            add.append(1)
            res.append(add)
            pre = res[-1]
        return res   