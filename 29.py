class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend > 0) is (divisor > 0)
        res = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            i = 1
            temp = divisor
            while dividend >= temp:
                dividend = dividend - temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = - res
        return min(max(-2147483648, res), 2147483647)