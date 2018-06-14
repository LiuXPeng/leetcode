class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]*(rowIndex + 1)
        for _ in range(rowIndex):
            k = _
            while k > 0:
                res[k] = res[k] + res[k - 1]
                k -= 1
        return res
