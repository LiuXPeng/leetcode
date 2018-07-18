class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        if n == 0:
            return res
        for i in range(n):
            ad = pow(2, i)
            temp = res[::-1]
            for j in range(len(temp)):
                temp[j] += ad
            res += temp
        return res