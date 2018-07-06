class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        tag = False
        if x < 0:
            tag = True
        x = abs(x)
        while x > 0:
            res = res * 10 + x % 10
            x = x // 10
        if tag:
            res = -res
        if res > 2147483647 or res < -2147483648:
            return 0
        return res